# Lecture AI

[中文](./README_cn.md) | [English](./README.md)

AI 驱动的讲座笔记助手。上传或录制讲座音频，即可获得结构化笔记和任务提取 —— 由 OpenAI Whisper、DeepAgents 和多智能体 pipeline驱动。

## 功能特点

- **音频上传 & 录制** — 支持 MP3、WAV、MP4、M4A、FLAC 格式；或在浏览器中直接录制
- **音频处理** — 通过 PyDub 自动按文件大小分块
- **转录** — OpenAI Whisper 说话人分离
- **AI 处理 Pipeline** — DeepAgent 编排，两个子智能体：
  - **转录智能体** — 将原始转录文本整理为带说话人标签的格式
  - **笔记智能体** — 提取任务、截止日期、关键概念和时间线
- **PDF 导出** — 生成格式化的讲座笔记（访问摘要页面时自动生成）
- **聊天界面** — 直接在主页提问关于讲座的问题
- **多页面导航** — 通过侧边栏链接访问摘要页面和状态页面

## 系统架构

```
音频上传/录制
       │
       ▼
  音频分块（PyDub，≤5MB）
       │
       ▼
  Whisper 转录（说话人分离）
       │
       ▼
  聚合 ASR 输出
       │
       ▼
  DeepAgent Pipeline
       │
       ├── 转录智能体 → 带说话人标签的格式化文本
       │
       └── 笔记智能体 → 结构化讲座笔记 + 任务
       │
       ▼
  PDF 生成（markdown_pdf）
```

## 项目结构

```
Lecture_AI/
├── app.py                        # Streamlit Web 应用 — 主聊天页面（入口）
├── pages/
│   ├── summary.py                # 摘要页面 — 查看笔记并下载 PDF
│   ├── status.py                 # 状态页面 — 查看处理状态
│   └── readme_cn.py              # 中文自述文件页面
├── src/
│   ├── agent.py                  # DeepAgent 配置（编排器 + 2 个子智能体）
│   ├── utils.py                  # 核心工具函数（分块、ASR、pipeline）
│   ├── audio/
│   │   ├── processor.py          # 音频分块与切片（PyDub）
│   │   └── transcriber.py        # OpenAI Whisper 转录
│   ├── pdf/
│   │   └── generator.py          # PDF 生成（markdown_pdf）
│   └── prompt/
│       ├── orchestration_agent_system_prompt.md
│       ├── transcription_agent_system_prompt.md
│       └── key_note_agent_system_prompt.md
└── lecture_recording/           # 讲座数据工作目录
    └── [lecture_name]/
        ├── raw/                  # 原始上传音频
        ├── chunks/               # 分块音频
        ├── asr/                  # 各分块 ASR 输出
        ├── [lecture_name]_formatted.md
        ├── [lecture_name]_summary.md
        └── [lecture_name]_summary.pdf
```

## 安装

1. 安装依赖：
```bash
pip install -e .
```

2. 配置环境变量（复制 `.env_example` 到 `.env` 并填写）：
```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
OPENROUTER_API_KEY=your_openrouter_key   # 可选
ROOT_DIR="Your ROOT DIR"
```

3. 运行应用：
```bash
streamlit run app.py        
```

## 使用说明

### 主页 — 聊天
1. 在浏览器中打开 Streamlit 提供的本地 URL
2. 选择输入方式 — 上传音频文件或实时录制
3. 点击 **🚀 Pre-Process Lecture**
4. 在聊天界面直接提问关于讲座的问题

### 摘要页面
- 通过侧边栏 **📚 Summaries** 链接进入
- 选择讲座名称查看生成的笔记
- PDF 首次访问时自动生成；点击按钮下载

### 状态页面
- 通过侧边栏 **📋 Status** 链接进入
- 查看所有讲座的处理状态（原始音频、分块、ASR、格式化、摘要）

## 依赖

- `streamlit` — Web UI
- `deepagents` — 多智能体编排与子智能体
- `openai` — Whisper 转录 API
- `pydub` — 音频文件处理
- `markdown-pdf` — Markdown 转 PDF
- `python-dotenv` — 环境变量管理
