# Azure OpenAI API Parameter Support Report

**Test Date:** 2026-01-30  
**API Version:** v1 (Official Recommendation)  
**Total Models Tested:** 18

---

## Executive Summary

This report provides a comprehensive analysis of parameter support across Azure OpenAI models (GPT-4.1, GPT-5, GPT-5.1, GPT-5.2 series) using the official v1 API.

### Key Findings

1. **Responses API** - Recommended for production use
   - More stable and feature-rich
   - Better parameter support across models

2. **Chat Completions API** - Available but limited
   - Basic functionality works
   - Some parameter restrictions on newer models

3. **Model Evolution**
   - GPT-5.1 and GPT-5.2: Best feature support
   - GPT-4.1: Stable but limited reasoning capabilities

## Parameter Support Matrix

Quick reference for parameter support across all models:

### Responses API (Recommended)

| Model | temperature | top_p | max_tokens | reasoning | instructions |
|-------|-------------|-------|------------|-----------|-------------|
| gpt-4.1-mini | ✅ | - | - | ❌ | - |
| gpt-4.1-nano | ✅ | - | - | ❌ | - |
| gpt-4.1 | ✅ | - | - | ❌ | - |
| gpt-5-chat | ✅ | - | - | ❌ | - |
| gpt-5-chat | ✅ | - | - | ❌ | - |
| gpt-5-codex | ❌ | - | - | ✅ | - |
| gpt-5-mini | ❌ | - | - | ✅ | - |
| gpt-5-nano | ❌ | - | - | ✅ | - |
| gpt-5-pro | ❌ | - | - | ⚠️ | - |
| gpt-5.1-chat | ❌ | - | - | ⚠️ | - |
| gpt-5.1-codex-max | ❌ | - | - | ✅ | - |
| gpt-5.1-codex-mini | ❌ | - | - | ✅ | - |
| gpt-5.1-codex | ❌ | - | - | ✅ | - |
| gpt-5.1 | ✅ | - | - | ✅ | - |
| gpt-5.2-chat | ❌ | - | - | ⚠️ | - |
| gpt-5.2-codex | ❌ | - | - | ✅ | - |
| gpt-5.2 | ✅ | - | - | ✅ | - |
| gpt-5 | ❌ | - | - | ✅ | - |

### Chat Completions API

| Model | temperature | top_p | max_tokens |
|-------|-------------|-------|------------|
| gpt-4.1-mini | ❌ | ❌ | - |
| gpt-4.1-nano | ❌ | ❌ | - |
| gpt-4.1 | ✅ | ✅ | - |
| gpt-5-chat | ❌ | ❌ | - |
| gpt-5-chat | ❌ | ❌ | - |
| gpt-5-codex | ❌ | ❌ | - |
| gpt-5-mini | ⚠️ | ❌ | - |
| gpt-5-nano | ❌ | ❌ | - |
| gpt-5-pro | ❌ | ❌ | - |
| gpt-5.1-chat | ❌ | ❌ | - |
| gpt-5.1-codex-max | ❌ | ❌ | - |
| gpt-5.1-codex-mini | ❌ | ❌ | - |
| gpt-5.1-codex | ❌ | ❌ | - |
| gpt-5.1 | ❌ | ❌ | - |
| gpt-5.2-chat | ❌ | ❌ | - |
| gpt-5.2-codex | ❌ | ❌ | - |
| gpt-5.2 | ❌ | ❌ | - |
| gpt-5 | ❌ | ❌ | - |

**Legend:** ✅ Supported | ❌ Not Supported | ⚠️ Limited/Partial Support


---

## GPT-4.1 Series

### gpt-4.1-mini

**Version:** 2025-04-14

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`

**Unsupported Parameters:**
- ❌ `reasoning` - Parameter not supported

---

### gpt-4.1-nano

**Version:** 2025-04-14

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`

**Unsupported Parameters:**
- ❌ `reasoning` - Parameter not supported

---

### gpt-4.1

**Version:** 2025-04-14

#### Chat Completions API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`
- ✅ `top_p`
- ✅ `max_completion_tokens`

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`

**Unsupported Parameters:**
- ❌ `reasoning` - Parameter not supported

---

## GPT-5 Series

### gpt-5-chat

**Version:** 2025-08-07

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`

**Unsupported Parameters:**
- ❌ `reasoning` - Parameter not supported

---

### gpt-5-chat

**Version:** 2025-10-03

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`

**Unsupported Parameters:**
- ❌ `reasoning` - Parameter not supported

---

### gpt-5-codex

**Version:** 2025-09-15

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5-mini

**Version:** 2025-08-07

#### Chat Completions API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `max_completion_tokens`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter value not supported
- ❌ `top_p` - Parameter not supported

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5-nano

**Version:** 2025-08-07

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5-pro

**Version:** 2025-10-06

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported
- ❌ `reasoning` - Parameter value not supported

---

### gpt-5

**Version:** 2025-08-07

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

## GPT-5.1 Series

### gpt-5.1-chat

**Version:** 2025-11-13

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported
- ❌ `reasoning` - Parameter value not supported

---

### gpt-5.1-codex-max

**Version:** 2025-12-04

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5.1-codex-mini

**Version:** 2025-11-13

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5.1-codex

**Version:** 2025-11-13

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5.1

**Version:** 2025-11-13

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`
- ✅ `reasoning`

---

## GPT-5.2 Series

### gpt-5.2-chat

**Version:** 2025-12-11

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported
- ❌ `reasoning` - Parameter value not supported

---

### gpt-5.2-codex

**Version:** 2026-01-14

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `reasoning`

**Unsupported Parameters:**
- ❌ `temperature` - Parameter not supported

---

### gpt-5.2

**Version:** 2025-12-11

#### Chat Completions API

**Status:** ⚠️ Limited availability

#### Responses API

**Status:** ✅ Available

**Supported Parameters:**
- ✅ `temperature`
- ✅ `reasoning`

---

## Error Reference

Common error messages and their meanings:

| Error Message | Meaning |
|---------------|----------|
| `Parameter not supported` | This parameter is not available for this model |
| `Parameter value not supported` | The parameter is available but the specific value is not supported |
| `Operation not supported by this model` | This API operation is not supported by the model |

---

## Technical Implementation

### Recommended API Setup (v1)

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

# Responses API (Recommended)
response = client.responses.create(
    model="gpt-5.1",
    input="Your prompt"
)

# Chat Completions API
response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Key Benefits of v1 API

- ✅ No need to specify `api-version`
- ✅ Automatic token refresh
- ✅ Compatible with OpenAI client
- ✅ Future-proof implementation

