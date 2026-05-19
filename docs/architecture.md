# Architecture Deep Dive

## How MCP Communication Works

```python
# 1. User types "ls"
# 2. Script creates JSON-RPC request
request = {
    "jsonrpc": "2.0",
    "method": "tools/call", 
    "params": {
        "name": "list_directory",
        "arguments": {"path": "/home/user/Desktop"}
    }
}
```

# 3. Sends to MCP server via stdin
# 4. Receives real file list via stdout
# 5. Displays to user EOF

## Why Subprocess Instead of Direct API?

MCP servers communicate over stdio (standard input/output), not HTTP. This is by design:

   -  Security - No network ports exposed

   -  Simplicity - No authentication needed for local use

   -  Performance - Lower latency than HTTP

## Memory Optimization

Tinyllama (637MB) was chosen because:

    - Fits in your 1.6GB available RAM

    - Leaves room for system processes

    - Still provides reasonable intelligence

## Future Extensibility

The MCP protocol supports:

    - Multiple servers (filesystem, database, web)

    - Tool chaining (server A → server B)

    - Resource subscriptions (live file watching)
