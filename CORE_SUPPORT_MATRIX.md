# Azure OpenAI Reasoning Models - 核心支持情况

---

## 1️⃣ 模型 API 支持情况

### 完整支持矩阵

| 模型 | Chat Completions API | Responses API | 备注 |
|------|---------------------|--------------|------|
| **gpt-5.2** | ✅ 支持 | ✅ 支持 | 全功能支持 |
| **gpt-5.2-codex** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5.1** | ✅ 支持 | ✅ 支持 | 全功能支持 |
| **gpt-5.1-chat** | ✅ 支持 | ✅ 支持 | 全功能支持 |
| **gpt-5.1-codex-max** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5.1-codex** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5.1-codex-mini** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5-pro** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5-codex** | ❌ OperationNotSupported | ✅ 支持 | 仅 Responses API |
| **gpt-5** | ✅ 支持 | ✅ 支持 | 全功能支持 |
| **gpt-5-mini** | ✅ 支持 | ✅ 支持 | 全功能支持 |
| **gpt-5-nano** | ✅ 支持 | ✅ 支持 | 全功能支持 |

**统计：**
- **Chat Completions API：** 6/12 支持 (50%)
- **Responses API：** 12/12 支持 (100%)
- **双 API 支持：** 6 个模型
- **仅 Responses API：** 6 个模型（所有 -codex 和 gpt-5-pro）

---

### API 要求

| API 类型 | 最低 API Version | Endpoint |
|---------|-----------------|----------|
| Chat Completions API | 2024-12-01-preview | `/openai/deployments/{deployment}/chat/completions` |
| Responses API | 2025-03-01-preview | `/openai/v1/responses` |

---

## 2️⃣ 参数支持情况

### 2.1 Reasoning Effort 支持

#### Chat Completions API 模型（6个）

| 模型 | low | medium | high | none | 备注 |
|------|-----|--------|------|------|------|
| gpt-5.2 | ✅ | ✅ | ✅ | ❌ | 标准三级 |
| gpt-5.1 | ✅ | ✅ | ✅ | ✅ | 支持 none (默认) |
| gpt-5.1-chat | ✅ | ✅ | ✅ | ❌ | 标准三级 |
| gpt-5 | ✅ | ✅ | ✅ | ❌ | 标准三级 |
| gpt-5-mini | ✅ | ✅ | ✅ | ❌ | 标准三级 |
| gpt-5-nano | ✅ | ✅ | ✅ | ❌ | 标准三级 |

#### Responses API 专用模型（6个）

| 模型 | low | medium | high | xhigh | none | 备注 |
|------|-----|--------|------|-------|------|------|
| gpt-5.2-codex | ✅ | ✅ | ✅ | ✅ | ❌ | 支持超高推理 |
| gpt-5.1-codex-max | ✅ | ✅ | ✅ | ✅ | ❌ | 支持超高推理 |
| gpt-5.1-codex | ✅ | ✅ | ✅ | ❌ | ❌ | 标准三级 |
| gpt-5.1-codex-mini | ✅ | ✅ | ✅ | ❌ | ❌ | 标准三级 |
| gpt-5-pro | ❌ | ❌ | ✅ | ❌ | ❌ | 仅 high |
| gpt-5-codex | ✅ | ✅ | ✅ | ❌ | ❌ | 标准三级 |

**关键发现：**
- ✅ **支持 xhigh（超高推理）：** 仅 gpt-5.2-codex, gpt-5.1-codex-max
- ✅ **支持 none：** 仅 gpt-5.1
- ⚠️ **仅支持 high：** gpt-5-pro（最受限）

---

### 2.2 Temperature 支持

| 模型 | temperature=1.0 (默认) | 自定义值 (如 0.7) | 支持范围 |
|------|----------------------|----------------|---------|
| gpt-5.2 | ✅ | ✅ | 0.0 - 2.0 |
| gpt-5.1 | ✅ | ✅ | 0.0 - 2.0 |
| gpt-5.1-chat | ✅ | ❌ | 仅 1.0 |
| gpt-5 | ✅ | ❌ | 仅 1.0 |
| gpt-5-mini | ✅ | ❌ | 仅 1.0 |
| gpt-5-nano | ✅ | ❌ | 仅 1.0 |
| *所有 -codex 模型* | ✅ | ❌ | 仅 1.0 |
| gpt-5-pro | ✅ | ❌ | 仅 1.0 |

**支持自定义 Temperature 的模型：** 仅 2/12 (gpt-5.2, gpt-5.1)

**错误信息示例：**
```
"Unsupported value: 'temperature' does not support 0.7 with this model. 
 Only the default (1) value is supported."
```

---

### 2.3 Image Input (Vision) 支持

| 模型 | Chat API | Responses API |
|------|---------|--------------|
| **gpt-5.2** | ✅ | ✅ |
| **gpt-5.2-codex** | N/A | ✅ |
| **gpt-5.1** | ✅ | ✅ |
| **gpt-5.1-chat** | ✅ | ✅ |
| **gpt-5.1-codex-max** | N/A | ✅ |
| **gpt-5.1-codex** | N/A | ✅ |
| **gpt-5.1-codex-mini** | N/A | ✅ |
| **gpt-5-pro** | N/A | ✅ |
| **gpt-5-codex** | N/A | ✅ |
| **gpt-5** | ✅ | ✅ |
| **gpt-5-mini** | ✅ | ✅ |
| **gpt-5-nano** | ✅ | ✅ |

**所有 12 个模型都支持 Image Input！** ✅

---

### 2.4 Structured Outputs (JSON mode) 支持

| 模型类型 | 支持情况 | 备注 |
|---------|---------|------|
| **所有 Chat API 模型** (6个) | ✅ 完全支持 | JSON mode 可用 |
| **Responses API 专用模型** (6个) | ✅ 完全支持 | JSON mode 可用 |

**支持率：** 12/12 (100%)

---

### 2.5 Developer Messages 支持

| 模型类型 | 支持情况 | 备注 |
|---------|---------|------|
| **所有 Chat API 模型** (6个) | ✅ 完全支持 | developer role 可用 |
| **Responses API 专用模型** (6个) | ✅ 完全支持 | developer role 可用 |

**支持率：** 12/12 (100%)

---

## 📊 快速参考表

### 按功能需求选择模型

| 需求 | 推荐模型 | 备注 |
|------|---------|------|
| **需要 Chat Completions API** | gpt-5.2, gpt-5.1, gpt-5.1-chat, gpt-5, gpt-5-mini, gpt-5-nano | 6 个模型 |
| **需要自定义 Temperature** | gpt-5.2, gpt-5.1 | 仅 2 个模型 |
| **需要超高推理 (xhigh)** | gpt-5.2-codex, gpt-5.1-codex-max | 仅 2 个模型 |
| **需要 Vision（Image Input）** | 所有 12 个模型都支持 | 100% 支持 |
| **代码生成任务** | gpt-5.1-codex, gpt-5-codex | 性能稳定 |
| **最高推理能力** | gpt-5.2-codex, gpt-5.1-codex-max | 支持 xhigh |

### 避免使用的场景

| 模型 | 避免场景 | 原因 |
|------|---------|------|
| **所有 -codex 和 gpt-5-pro** | Chat Completions API | 不支持，返回 OperationNotSupported |

---

## 🔑 关键结论

### API 支持
- ✅ **所有 12 个模型支持 Responses API** (100%)
- ✅ **6 个模型支持 Chat Completions API** (50%)
- ⚠️ **6 个模型仅支持 Responses API**（-codex 系列 + gpt-5-pro）

### 参数支持
- ✅ **Reasoning Effort：** 所有模型至少支持 low/medium/high
- ✅ **Image Input：** 所有 12 个模型都支持（100%）
- ✅ **Structured Outputs：** 所有模型支持（100%）
- ✅ **Developer Messages：** 所有模型支持（100%）
- ⚠️ **Temperature：** 仅 2 个模型支持自定义值（17%）

### 特殊能力
- **xhigh 推理：** 仅 gpt-5.2-codex, gpt-5.1-codex-max
- **none 推理：** 仅 gpt-5.1
- **自定义 Temperature：** 仅 gpt-5.2, gpt-5.1

---

**最后更新：** 2026-02-02
