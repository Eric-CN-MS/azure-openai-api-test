#!/usr/bin/env python3
"""
生成参数支持汇总表
"""

import json
import glob
import os
from collections import defaultdict

def load_all_test_results():
    """加载所有测试结果"""
    base_path = '/home/azureuser/clawd/azure-openai-tester/reports'
    
    results = defaultdict(lambda: {'chat': None, 'responses': None})
    
    for series in ['gpt-4.1', 'gpt-5', 'gpt-5.1', 'gpt-5.2']:
        series_dir = f'{base_path}/{series}'
        if not os.path.exists(series_dir):
            continue
        
        for filepath in glob.glob(f'{series_dir}/*.json'):
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            model = data['metadata']['model_name']
            version = data['metadata']['model_version']
            api_type = data['metadata']['api_type']
            
            key = f"{model}@{version}"
            results[key][api_type] = data
    
    return results

def create_summary_table():
    """创建参数支持汇总表"""
    results = load_all_test_results()
    
    # 参数列表
    params = ['temperature', 'top_p', 'max_completion_tokens', 'reasoning', 'instructions']
    
    table = "## Parameter Support Matrix\n\n"
    table += "Quick reference for parameter support across all models:\n\n"
    table += "### Responses API (Recommended)\n\n"
    table += "| Model | temperature | top_p | max_tokens | reasoning | instructions |\n"
    table += "|-------|-------------|-------|------------|-----------|-------------|\n"
    
    for model_key in sorted(results.keys()):
        model_name = model_key.split('@')[0]
        data = results[model_key]
        
        if not data['responses']:
            continue
        
        row = f"| {model_name} |"
        
        for param in params:
            support = check_parameter_support(data['responses'], param)
            row += f" {support} |"
        
        table += row + "\n"
    
    table += "\n"
    table += "### Chat Completions API\n\n"
    table += "| Model | temperature | top_p | max_tokens |\n"
    table += "|-------|-------------|-------|------------|\n"
    
    chat_params = ['temperature', 'top_p', 'max_completion_tokens']
    
    for model_key in sorted(results.keys()):
        model_name = model_key.split('@')[0]
        data = results[model_key]
        
        if not data['chat']:
            continue
        
        row = f"| {model_name} |"
        
        for param in chat_params:
            support = check_parameter_support(data['chat'], param)
            row += f" {support} |"
        
        table += row + "\n"
    
    table += "\n**Legend:** ✅ Supported | ❌ Not Supported | ⚠️ Limited/Partial Support\n\n"
    
    return table

def check_parameter_support(api_data, param_name):
    """检查参数支持状态"""
    if not api_data:
        return "⚠️"
    
    results = api_data['results']
    
    # 查找相关测试
    for result in results:
        test_name = result['test_name'].lower()
        
        # 匹配参数名
        param_check = param_name.replace('_', ' ').replace('max completion tokens', 'max tokens')
        
        if param_check in test_name or param_name in test_name:
            if result['success']:
                return "✅"
            else:
                # 检查是否是部分支持
                error = result.get('error', {})
                message = error.get('message', '')
                if 'value' in message.lower():
                    return "⚠️"
                return "❌"
    
    return "-"

def main():
    table = create_summary_table()
    
    # 插入到报告开头
    with open('API_PARAMETER_SUPPORT.md', 'r') as f:
        content = f.read()
    
    # 在 Executive Summary 后插入
    parts = content.split('---\n\n## GPT-4.1 Series')
    
    new_content = parts[0] + table + "\n---\n\n## GPT-4.1 Series" + parts[1]
    
    with open('API_PARAMETER_SUPPORT.md', 'w') as f:
        f.write(new_content)
    
    print("✅ Summary table added to report")

if __name__ == '__main__':
    main()
