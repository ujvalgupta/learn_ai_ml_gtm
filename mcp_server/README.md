So now we actually have the complete AI + MCP architecture.

Pi = AI agent harness / MCP Host
DeepSeek V4 Flash = LLM doing the reasoning
Pi's MCP client/adapter = communicates with MCP servers
Our Python app = MCP Server
score_company() = MCP Tool
Python code inside the tool = actual GTM logic

Pi's ecosystem has documented DeepSeek V4 Flash configurations, and the Pi MCP adapter is specifically designed to let Pi use MCP servers.

User
 ↓
Pi
 ↓
DeepSeek V4 Flash
 ↓
LLM decides to use tool
 ↓
Pi MCP Client
 ↓
MCP protocol
 ↓
Python MCP Server
 ↓
score_company()
 ↓
GTM logic
 ↓
Tool result
 ↓
Pi
 ↓
DeepSeek
 ↓
Natural-language response
 ↓
User
