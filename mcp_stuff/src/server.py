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

@mcp.tool(
name = "score_company",
description = "A utility that can help you score leads ( companies )",
tags = {"GTM" , "outbound"},
meta = {"sales":"marketing"}
)
def score_company(name:str, is_hiring:bool, funding:float) -> float:
    
    score = 0

    if is_hiring == True:
        score += 50
    
    if funding > 100000000:
        score += 50

    return score

if __name__ == "__main__":
    mcp.run()
