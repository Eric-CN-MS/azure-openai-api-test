# Azure OpenAI API Parameter Support Test

Comprehensive testing of parameter support across Azure OpenAI GPT-4.1, GPT-5, GPT-5.1, and GPT-5.2 series models using the official v1 API.

## 📊 Test Report

📄 **[API Parameter Support Report](API_PARAMETER_SUPPORT.md)** - Complete analysis of all 18 models

## 🎯 What's Tested

- **18 Models** across 4 series (GPT-4.1, GPT-5, GPT-5.1, GPT-5.2)
- **2 APIs**: Chat Completions API & Responses API
- **Key Parameters**: temperature, top_p, max_completion_tokens, reasoning, instructions

## 🔍 Quick Findings

### Recommended: Responses API ✅
- More stable across models
- Better parameter support
- Recommended for production

### Available: Chat Completions API ⚠️
- Basic functionality works
- Some parameter limitations on specific models

### Model Recommendations
- **GPT-5.1 / GPT-5.2**: Best feature support, includes reasoning
- **GPT-4.1**: Stable baseline, limited reasoning capabilities

## 📁 Repository Structure

```
.
├── API_PARAMETER_SUPPORT.md    # Main test report
├── generate_report.py          # Report generation script
└── README.md                   # This file
```

## 🔧 Technical Details

### v1 API Implementation

The tests use the official v1 API recommendation:

```python
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url="https://your-resource.openai.azure.com/openai/v1/",
    api_key=token_provider
)
```

### Benefits of v1 API
- ✅ No `api-version` parameter needed
- ✅ Automatic token refresh
- ✅ OpenAI client compatibility
- ✅ Future-proof

## 📅 Test Information

- **Test Date**: 2026-01-30
- **API Version**: v1 (Official)
- **Authentication**: Azure Managed Identity
- **Models Tested**: 18

## 📖 Reading the Report

The report is organized as:

1. **Executive Summary** - Key findings and recommendations
2. **Model-by-Model Results** - Detailed parameter support for each model
3. **Error Reference** - Common error messages explained
4. **Technical Implementation** - Code examples and setup

## ⚠️ Important Notes

- Tests focus on parameter support, not deployment timing issues
- All errors related to deployment availability have been filtered out
- Results reflect production-ready API capabilities

---

**Generated**: 2026-01-30  
**License**: MIT
