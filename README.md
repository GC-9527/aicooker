# personal_chief - AI私人厨师

一个基于AI的智能私人厨师应用，可以根据用户上传的食材图片推荐个性化食谱。

## 功能特点

- 🍳 上传食材图片，AI智能识别食材
- 📋 智能推荐个性化食谱
- 🤖 基于Langchain的AI代理架构
- 📱 现代化的Web界面（Next.js）
- 💾 数据库持久化对话记录
- ☁️ 阿里云OSS图片存储

## 技术栈

### 后端
- **FastAPI** - Web框架
- **Langchain** - AI应用框架
- **Langgraph** - 工作流编排
- **SQLite** - 数据库
- **阿里云OSS** - 对象存储

### 前端
- **Next.js** - React框架
- **React** - UI库

## 项目结构

```
aicooker/
├── app/                          # 主应用
│   ├── main.py                  # FastAPI入口
│   ├── api/
│   │   └── v1/
│   │       ├── chat.py         # 聊天接口
│   │       └── oss.py          # OSS上传接口
│   ├── agents/
│   │   └── personal_chief.py   # AI厨师代理
│   ├── models/
│   │   └── schemas.py          # 数据模型
│   ├── common/
│   │   └── logger.py           # 日志
│   ├── db/
│   │   └── personal_chief.db   # SQLite数据库
│   └── static/                 # 前端静态文件
├── Langchain/                   # Langchain学习和实验
│   ├── aicooker.ipynb
│   ├── aicooker.py
│   └── test_api.py
├── langgraph.json              # Langgraph配置
└── README.md
```

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 18+

### 安装依赖

```bash
# 后端依赖
pip install -r requirements.txt
```

### 配置环境变量

在 `Langchain/.env` 文件中配置：

```env
# LLM配置
LLM_PROVIDER=ollama
OLLAMA_MODEL=gemma4:e4b:latest
OLLAMA_BASE_URL=http://localhost:11434

# 阿里云OSS
OSS_ACCESS_KEY_ID=your_access_key
OSS_ACCESS_KEY_SECRET=your_secret
OSS_BUCKET=your_bucket
```

### 运行项目

```bash
# 启动后端服务
cd app
python main.py
```

## 许可证

MIT License
