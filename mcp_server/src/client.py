import asyncio
from fastmcp import Client

client = Client("server.py")

async def main():
    async with client:
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        result = await client.call_tool("greeting_tool", {"name": "UGupta"})

        print(result)

asyncio.run(main())
