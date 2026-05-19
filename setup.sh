#!/bin/bash
set -e  # Exit on error

echo "🔧 Setting up AI Agent Environment"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Ubuntu version
if ! grep -q "Ubuntu" /etc/os-release; then
    echo -e "${YELLOW}⚠️  This script is tested on Ubuntu. YMMV on other distros.${NC}"
fi

# Check Python
echo -n "Checking Python... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✓ $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Not found${NC}"
    echo "Installing Python..."
    sudo apt update && sudo apt install -y python3 python3-pip
fi

# Check pip
echo -n "Checking pip... "
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${RED}✗ Installing...${NC}"
    sudo apt install -y python3-pip
fi

# Install Ollama
echo -n "Checking Ollama... "
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Already installed${NC}"
else
    echo -e "${YELLOW}Installing Ollama...${NC}"
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Check Node.js/npx for MCP
echo -n "Checking npx... "
if command -v npx &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${YELLOW}Installing Node.js...${NC}"
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt install -y nodejs
fi

# Pull model (this takes time)
echo ""
echo "📦 Pulling tinyllama model (637MB)..."
ollama pull tinyllama

# Install Python packages
echo ""
echo "📦 Installing Python dependencies..."
pip3 install --user requests

# Make script executable
chmod +x ai_agent.py

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "🚀 To run your AI agent:"
echo "   python3 ai_agent.py"
echo ""
echo "📖 For documentation:"
echo "   cat README.md"
