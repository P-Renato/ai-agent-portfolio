# 🤖 Local AI Agent with MCP Filesystem Access

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-0.6+-green.svg)](https://ollama.ai)

## 🎯 Project Overview

A **production-ready local AI agent** that bridges the gap between Large Language Models and your actual filesystem using the **Model Context Protocol (MCP)**.

Unlike chatbot demos that hallucinate file operations, this agent executes **real** filesystem operations while keeping your data 100% local and private.

## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────┐
│ User Interface (CLI) │
└─────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ Command Router │
│ ┌──────────────┴──────────────┐ │
│ │ │ │
│ ▼ ▼ │
│ [MCP Tools] [Ollama LLM] │
│ - list_directory - tinyllama (637MB) │
│ - read_file - 100% local inference │
│ - write_file (planned) - No API costs │
│ │ │ │
│ └──────────────┬──────────────┘ │
│ ▼ │
│ [Your Filesystem] │
└─────────────────────────────────────────────────────────────┘
text


## ✨ Features

| Feature | Status | Description |
|---------|--------|-------------|
| Real filesystem listing | ✅ | Shows ACTUAL files, not hallucinations |
| File reading | ✅ | Read any text file from allowed directories |
| Local LLM inference | ✅ | Runs on CPU, no GPU required |
| Privacy-first | ✅ | Zero data sent to cloud |
| MCP standard compliant | ✅ | Uses Model Context Protocol |
| Write files | 🚧 Planned | Safe file creation with approval |
| Search files | 🚧 Planned | Pattern-based file search |
| Web search integration | 🚧 Planned | Optional external tool |

## 🚀 Quick Start (5 minutes)

### Prerequisites

- **Ubuntu 22.04+** (or any Linux with Python 3.12+)
- **8GB RAM minimum** (4GB free after OS)
- **Internet** for initial download only

### One-Command Setup

```bash
git clone https://gitlab.com/your-username/ai-agent.git
cd ai-agent
chmod +x setup.sh
./setup.sh

Manual Setup (if you prefer)
bash

# 1. Install Ollama (local LLM runtime)
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull the optimized model
ollama pull tinyllama

# 3. Install Python dependencies
pip3 install --user requests

# 4. Run the agent
python3 ai_agent.py

💡 Usage Examples
List files (MCP tool call)
bash

[/home/user/Desktop]> ls
[DIR] projects
[FILE] resume.pdf
[FILE] notes.txt

Read a file
bash

[/home/user/Desktop]> read notes.txt
📄 Reading: /home/user/Desktop/notes.txt
Content: Meeting notes from DevOps team...

Ask the AI questions
bash

[/home/user/Desktop]> ask What is the difference between Docker and containerd?
AI: Docker includes containerd as its container runtime...

Navigate directories
bash

[/home/user/Desktop]> cd /tmp
[/tmp]> ls
[FILE] temp_file.txt

🔧 Customization
Switch to a smarter model
bash

ollama pull phi          # 1.6GB, better reasoning
ollama pull llama3.2:1b  # 1.3GB, balanced

Then edit ai_agent.py line 22:
python

"model": "phi",  # Change from "tinyllama"

Add write_file capability

See docs/extending.md for adding new MCP tools.
📊 Performance Metrics
Metric	Value
Memory usage (idle)	~100 MB
Memory with tinyllama	~737 MB
Response time (simple query)	2-5 seconds
Model download size	637 MB
First-time setup time	~3 minutes
🛠️ Technology Stack
Component	Technology	Why
LLM Runtime	Ollama	Best local inference, easy to use
Model	tinyllama	Optimized for resource constraints
Tool Protocol	MCP	Industry standard (Anthropic, OpenAI)
Language	Python 3.12	Ubiquitous, easy to extend
IPC	JSON-RPC	Standard for MCP communication
📈 Skills Demonstrated

This project showcases:

    Local LLM Deployment - Running models on consumer hardware

    MCP Integration - Implementing emerging AI-tool standard

    Subprocess Management - Safe subprocess communication

    Resource Optimization - Working within memory constraints

    System Integration - Bridging AI with real filesystem

    Documentation - Professional, recruiter-friendly docs

    Reproducible Builds - One-command setup for anyone

🤔 Why This Matters

Most "AI agents" you see online:

    ❌ Require expensive API keys

    ❌ Send your data to the cloud

    ❌ Hallucinate file operations

    ❌ Can't actually DO anything

This agent:

    ✅ Runs 100% locally (free, private)

    ✅ Executes REAL operations

    ✅ Follows MCP standard (future-proof)

    ✅ Teaches transferable skills

🐛 Troubleshooting
"Ollama not responding"
bash

# Check if Ollama is running
ps aux | grep ollama

# Start it manually
ollama serve &

"npx: command not found"
bash

# npx comes with Node.js
sudo apt install nodejs npm

"Address already in use"
bash

# Kill existing Ollama process
pkill ollama
ollama serve &

See docs/troubleshooting.md for more.
📝 License

MIT - Use freely for learning and portfolios.
🙏 Acknowledgments

    Ollama for local LLM runtime

    MCP Specification for the tool protocol

    Anthropic for pioneering MCP

📧 Contact

Built by [Your Name] - DevOps Engineer in training

    GitLab: @your-username

    LinkedIn: /in/your-linkedin

⭐ Star this repo if you find it useful!
