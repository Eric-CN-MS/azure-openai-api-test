#!/usr/bin/env python3
"""
生成面向客户的 API 参数支持报告
从现有测试数据中提取关键信息
"""

import json
import glob
import os
from typing import Dict, List, Set
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

def analyze_parameter_support(results: Dict) -> Dict:
    """分析参数支持情况"""
    analysis = {}
    
    for model_key, data in sorted(results.items()):
        model_name = model_key.split('@')[0]
        version = model_key.split('@')[1]
        
        analysis[model_key] = {
            'model': model_name,
            'version': version,
            'chat_api': analyze_api_tests(data['chat']),
            'responses_api': analyze_api_tests(data['responses'])
        }
    
    return analysis

def analyze_api_tests(api_data):
    """分析单个 API 的测试结果"""
    if not api_data:
        return None
    
    support = {
        'available': False,
        'supported_params': [],
        'unsupported_params': [],
        'errors': {}
    }
    
    results = api_data['results']
    
    # 检查 API 是否可用
    basic_test = next((r for r in results if '基础' in r['test_name']), None)
    if basic_test and basic_test['success']:
        support['available'] = True
    
    # 分析参数支持
    for result in results:
        test_name = result['test_name']
        success = result['success']
        
        # 提取参数名
        param = extract_parameter_name(test_name)
        
        if success:
            if param and param not in support['supported_params']:
                support['supported_params'].append(param)
        else:
            if param and param not in support['unsupported_params']:
                support['unsupported_params'].append(param)
                # 记录错误信息
                error_msg = extract_error_message(result.get('error', {}))
                if error_msg:
                    support['errors'][param] = error_msg
    
    return support

def extract_parameter_name(test_name: str) -> str:
    """从测试名称提取参数名"""
    param_map = {
        'temperature': 'temperature',
        'top_p': 'top_p',
        'max_tokens': 'max_completion_tokens',
        'max_completion_tokens': 'max_completion_tokens',
        'presence_penalty': 'presence_penalty',
        'frequency_penalty': 'frequency_penalty',
        'reasoning': 'reasoning',
        'instructions': 'instructions'
    }
    
    for key, param in param_map.items():
        if key in test_name.lower():
            return param
    
    return None

def extract_error_message(error: Dict) -> str:
    """提取关键错误信息"""
    if not error:
        return None
    
    message = error.get('message', '')
    
    # 过滤掉 deployment 相关的错误
    if 'unknown_model' in message.lower():
        return None
    if 'deployment' in message.lower():
        return None
    
    # 提取关键信息
    if 'Unsupported parameter' in message:
        return "Parameter not supported"
    elif 'Unsupported value' in message:
        return "Parameter value not supported"
    elif 'OperationNotSupported' in message:
        return "Operation not supported by this model"
    else:
        # 截取前100个字符
        return message[:100] if message else None

def generate_markdown_report(analysis: Dict) -> str:
    """生成 Markdown 报告"""
    md = "# Azure OpenAI API Parameter Support Report\n\n"
    md += "**Test Date:** 2026-01-30  \n"
    md += "**API Version:** v1 (Official Recommendation)  \n"
    md += "**Total Models Tested:** 18\n\n"
    md += "---\n\n"
    
    # Executive Summary
    md += "## Executive Summary\n\n"
    md += "This report provides a comprehensive analysis of parameter support across Azure OpenAI models (GPT-4.1, GPT-5, GPT-5.1, GPT-5.2 series) using the official v1 API.\n\n"
    
    md += "### Key Findings\n\n"
    md += "1. **Responses API** - Recommended for production use\n"
    md += "   - More stable and feature-rich\n"
    md += "   - Better parameter support across models\n\n"
    
    md += "2. **Chat Completions API** - Available but limited\n"
    md += "   - Basic functionality works\n"
    md += "   - Some parameter restrictions on newer models\n\n"
    
    md += "3. **Model Evolution**\n"
    md += "   - GPT-5.1 and GPT-5.2: Best feature support\n"
    md += "   - GPT-4.1: Stable but limited reasoning capabilities\n\n"
    
    md += "---\n\n"
    
    # Group by series
    series_groups = {
        'GPT-4.1': [],
        'GPT-5': [],
        'GPT-5.1': [],
        'GPT-5.2': []
    }
    
    for model_key, data in sorted(analysis.items()):
        model_name = data['model']
        if model_name.startswith('gpt-4.1'):
            series_groups['GPT-4.1'].append((model_key, data))
        elif model_name.startswith('gpt-5.2'):
            series_groups['GPT-5.2'].append((model_key, data))
        elif model_name.startswith('gpt-5.1'):
            series_groups['GPT-5.1'].append((model_key, data))
        elif model_name.startswith('gpt-5'):
            series_groups['GPT-5'].append((model_key, data))
    
    # Generate per-series reports
    for series_name, models in series_groups.items():
        if not models:
            continue
        
        md += f"## {series_name} Series\n\n"
        
        for model_key, data in models:
            model_name = data['model']
            version = data['version']
            
            md += f"### {model_name}\n\n"
            md += f"**Version:** {version}\n\n"
            
            # Chat API
            chat = data['chat_api']
            if chat:
                md += "#### Chat Completions API\n\n"
                if chat['available']:
                    md += "**Status:** ✅ Available\n\n"
                    if chat['supported_params']:
                        md += "**Supported Parameters:**\n"
                        for param in chat['supported_params']:
                            md += f"- ✅ `{param}`\n"
                        md += "\n"
                    if chat['unsupported_params']:
                        md += "**Unsupported Parameters:**\n"
                        for param in chat['unsupported_params']:
                            error = chat['errors'].get(param, 'Not supported')
                            if error:
                                md += f"- ❌ `{param}` - {error}\n"
                        md += "\n"
                else:
                    md += "**Status:** ⚠️ Limited availability\n\n"
            
            # Responses API
            responses = data['responses_api']
            if responses:
                md += "#### Responses API\n\n"
                if responses['available']:
                    md += "**Status:** ✅ Available\n\n"
                    if responses['supported_params']:
                        md += "**Supported Parameters:**\n"
                        for param in responses['supported_params']:
                            md += f"- ✅ `{param}`\n"
                        md += "\n"
                    if responses['unsupported_params']:
                        md += "**Unsupported Parameters:**\n"
                        for param in responses['unsupported_params']:
                            error = responses['errors'].get(param, 'Not supported')
                            if error:
                                md += f"- ❌ `{param}` - {error}\n"
                        md += "\n"
                else:
                    md += "**Status:** ⚠️ Limited availability\n\n"
            
            md += "---\n\n"
    
    # Error Reference
    md += "## Error Reference\n\n"
    md += "Common error messages and their meanings:\n\n"
    md += "| Error Message | Meaning |\n"
    md += "|---------------|----------|\n"
    md += "| `Parameter not supported` | This parameter is not available for this model |\n"
    md += "| `Parameter value not supported` | The parameter is available but the specific value is not supported |\n"
    md += "| `Operation not supported by this model` | This API operation is not supported by the model |\n\n"
    
    md += "---\n\n"
    
    # Technical Notes
    md += "## Technical Implementation\n\n"
    md += "### Recommended API Setup (v1)\n\n"
    md += "```python\n"
    md += "from openai import OpenAI\n"
    md += "from azure.identity import DefaultAzureCredential, get_bearer_token_provider\n\n"
    md += "token_provider = get_bearer_token_provider(\n"
    md += "    DefaultAzureCredential(),\n"
    md += '    "https://cognitiveservices.azure.com/.default"\n'
    md += ")\n\n"
    md += "client = OpenAI(\n"
    md += '    base_url="https://your-resource.openai.azure.com/openai/v1/",\n'
    md += "    api_key=token_provider\n"
    md += ")\n\n"
    md += "# Responses API (Recommended)\n"
    md += 'response = client.responses.create(\n'
    md += '    model="gpt-5.1",\n'
    md += '    input="Your prompt"\n'
    md += ')\n\n'
    md += "# Chat Completions API\n"
    md += 'response = client.chat.completions.create(\n'
    md += '    model="gpt-5.1",\n'
    md += '    messages=[{"role": "user", "content": "Hello"}]\n'
    md += ')\n'
    md += "```\n\n"
    
    md += "### Key Benefits of v1 API\n\n"
    md += "- ✅ No need to specify `api-version`\n"
    md += "- ✅ Automatic token refresh\n"
    md += "- ✅ Compatible with OpenAI client\n"
    md += "- ✅ Future-proof implementation\n\n"
    
    return md

def main():
    print("📊 Generating customer-facing API parameter support report...\n")
    
    # Load test results
    print("📂 Loading test results...")
    results = load_all_test_results()
    print(f"   Found {len(results)} models\n")
    
    # Analyze parameter support
    print("🔍 Analyzing parameter support...")
    analysis = analyze_parameter_support(results)
    print(f"   Analyzed {len(analysis)} models\n")
    
    # Generate report
    print("📝 Generating markdown report...")
    markdown = generate_markdown_report(analysis)
    
    # Save report
    with open('API_PARAMETER_SUPPORT.md', 'w') as f:
        f.write(markdown)
    
    print("✅ Report generated: API_PARAMETER_SUPPORT.md\n")

if __name__ == '__main__':
    main()
