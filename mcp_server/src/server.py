from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool(
name = "greeting_tool",
description= "it's for greeting",
tags = {"intro","col"},
meta = {"hola" : "hello"}
)
def Greet (name:str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    mcp.run()
