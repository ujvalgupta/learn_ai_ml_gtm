1. Basic Python Quickly
    https://www.youtube.com/watch?v=fr1f84rg4Nw
    
    python3, pip etc install via apt
    creating a python venv, how to deactivate it, why is it needed
    python3 for a REPL
    pip for installing modules, then importing them
    importing math and using some functions from it
    variables and types
    string functions like capitalize, lower, upper etc
    list --> [1,2,3] , can change values
    type(int)
    tuple --> (1,2,3) , can't change values
    dictionary --> {"name" : "ujval", "surname" : "gupta"} .items() .keys()
    type casting like print (str(1) + "hello")
    indentations instead of brackets
    input() --> print(float(input()))
    usage of for, while etc
    using 'def' for defining functions
    try except for exception handling
    doing stuff in files, open() , read(), write()
    usage of pip freez, pip install for requirements.txt when you are shipping stuff to github or pulling stuff from there
    concept of coroutine, async, await, asyncio for asynchronous stuff

2. Let's understand MCP deeply and code stuff in Python related to it.

--> MCP was built by Anthropic
--> Protocols = rules = standards
--> There's a MCP host that has a bunch of MCP clients that uses MCP protocol to connect with MCP servers. MCP servers are the ones that actually have the capabilities.
--> MCP address a couple of needs of the LLM applications ( AI agents basically ). One is providing a standard way to get the external context and the next is to execute tool calls . Both of them are done by the MCP servers. The MCP servers basically advertises tools, its description, capabilities, I/O schema etc.
--> When the AI agents uses MCP client to invoke the tools advertised by MCP servers, its the MCP server that executes the tool calls.
--> Another primitive is resources. MCP server can provide these resources on demand and these are essentially read only files, docs.
--> Another primitive is Prompt templates that MCP server can provide.
--> APIs are a way for developers to use external services without building them from scratch. Seems to be a bit similar to MCP. How is it different ?
--> For APIs, there's a client and a server. Client triggers some API requests to the server which then sserves the request. A common example is RESTFul API
--> Both are client/server architecture based and offer a layer of abstraction so that you don't have to reinvent wheels.
--> A fundamental difference is that MCP was specifically built for AI agents but the APIs are general purpose.
--> Also, MCP allows for dynamic self discovery which means an agent can ask an MCP server on demand about the stuff it can provide and fix it's game plan accordingly. That is not the caase with RESTFul API.
--> A lot of MCP servers are just a wrapper on top of APIs exposed by a company. MCP servers kind of provide a way for external AI agents to talk to that company's services. For AI agents or AI native solutions, talking to an MCP server is more convenient compared to talking to the APIs directly.
--> If you think that AI agents can use the APIs directly, yes they can but then they need to know every single API of every external solution they wanna talk to and its not recommended that they are hard coded because it can change but using dynamic self discovery in case of MCP, agent can know about the capabilities on demand.
--> In case of APIs, the developers generally pre decide what the workflow looks like , they choose APIs, defined flow and write the code logic but that is not how the AI agents work. The task vary, so the plan to execute it has to be made on demand based on the capabilities exposed by the MCP server of the solution we are using
--> There's an MCP Inspector that can help in debugging and testing the MCP servers. 
