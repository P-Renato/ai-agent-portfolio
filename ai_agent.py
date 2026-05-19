#!/usr/bin/env python3
"""
Simple AI Agent with MCP Filesystem Tool
Works with Ollama and gives you real filesystem access
"""

import json
import subprocess
import sys
import os

# Try to import requests, install if not available
try:
    import requests
except ImportError:
    print("Installing requests module...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "requests"], check=True)
    import requests

def call_ollama(prompt):
    """Call Ollama with a prompt using native API"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 500
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json().get("response", "No response")
        else:
            return f"Error: Ollama returned {response.status_code}"
    except Exception as e:
        return f"Error calling Ollama: {e}"

def call_mcp_tool(tool_name, arguments):
    """Call an MCP tool directly using the filesystem server"""
    
    # First, check if we need to install the server
    mcp_request = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        },
        "id": 1
    }
    
    try:
        # Run the MCP server and send the request
        process = subprocess.Popen(
            ["npx", "-y", "@modelcontextprotocol/server-filesystem", "/home/dci-student/Desktop"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(json.dumps(mcp_request) + "\n", timeout=30)
        
        if stdout:
            result = json.loads(stdout)
            if "result" in result and "content" in result["result"]:
                content = result["result"]["content"][0]
                if content["type"] == "text":
                    return content["text"]
            elif "error" in result:
                return f"Tool error: {result['error']}"
        
        if stderr:
            return f"Server error: {stderr}"
            
        return "No result from tool"
        
    except subprocess.TimeoutExpired:
        process.kill()
        return "Tool call timed out"
    except Exception as e:
        return f"Error calling tool: {e}"

def list_directory(path):
    """List contents of a directory"""
    result = call_mcp_tool("list_directory", {"path": path})
    return result

def read_file(path):
    """Read a file's contents"""
    result = call_mcp_tool("read_text_file", {"path": path})
    return result

def main():
    print("\n" + "="*60)
    print("🤖 Simple AI Agent with Filesystem Access")
    print("="*60)
    print(f"Model: tinyllama (637MB)")
    print(f"Working directory: /home/dci-student/Desktop")
    print("-"*60)
    print("Commands:")
    print("  ls                    - List files in current directory")
    print("  ls <path>            - List files in specific directory")
    print("  read <filename>      - Read a file")
    print("  ask <question>       - Ask the AI a question")
    print("  help                 - Show this help")
    print("  quit / exit          - Exit the agent")
    print("-"*60)
    
    current_path = "/home/dci-student/Desktop"
    
    while True:
        try:
            user_input = input(f"\n[{current_path}]> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye! 👋")
                break
                
            elif user_input.lower() == "help":
                print("\nCommands:")
                print("  ls                    - List files in current directory")
                print("  ls <path>            - List files in specific directory")
                print("  read <filename>      - Read a file")
                print("  ask <question>       - Ask the AI a question")
                print("  help                 - Show this help")
                print("  quit / exit          - Exit the agent")
                
            elif user_input.lower().startswith("ls"):
                # Parse ls command
                parts = user_input.split(maxsplit=1)
                if len(parts) > 1:
                    target_path = parts[1]
                    if not target_path.startswith("/"):
                        target_path = os.path.join(current_path, target_path)
                else:
                    target_path = current_path
                
                print(f"📁 Listing: {target_path}")
                result = list_directory(target_path)
                print(result)
                
            elif user_input.lower().startswith("read "):
                filename = user_input[5:].strip()
                file_path = os.path.join(current_path, filename)
                print(f"📄 Reading: {file_path}")
                result = read_file(file_path)
                print(result)
                
            elif user_input.lower().startswith("ask "):
                question = user_input[4:].strip()
                print(f"🤔 Asking AI: {question}")
                print("-"*40)
                response = call_ollama(question)
                print(f"AI: {response}")
                
            elif user_input.lower().startswith("cd "):
                new_dir = user_input[3:].strip()
                if new_dir.startswith("/"):
                    current_path = new_dir
                else:
                    current_path = os.path.join(current_path, new_dir)
                # Normalize the path
                current_path = os.path.normpath(current_path)
                print(f"Changed directory to: {current_path}")
                
            else:
                # Treat as a question to the AI
                print(f"🤔 Asking AI...")
                print("-"*40)
                response = call_ollama(user_input)
                print(f"AI: {response}")
                
        except KeyboardInterrupt:
            print("\n\nUse 'quit' to exit")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
