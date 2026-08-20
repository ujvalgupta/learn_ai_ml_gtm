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

---------------

Specs for building the memory layer -->

1. For read , the flow will basically look like, user sends the message, we reformulate the query using a LLM call to refine it a bit, then we embed it using an embedding model, we get the vector now, we basically run a similarity search in the SQLite database and figure out top K vectors (plus it should be above a specific threshold). similarity search will be based on cosine similarity. we get the plain text from the top K vectors, make the final prompt using the system prompt, user input, previous messages and the context found. Do the main LLM call , get response, show it to user, and in async mode, also do write.

2. For write, we first do a LLM call to get if there are any new candidate facts by passing the entire prompt we sent to LLM in the read step and the LLM response as well . It gives us some facts and then for each of those candidate facts, we embed it , do a similarity search in the db, get the top k candidates ( plus they should pass a specific threshold ), we do an LLM API call for reconciliation, it returns annotations like new, duplicate, contradiction etc, for contradiction ones, we mark it as status=supersede by default all embeddings in the SQLite would be status=active and then we do the updations accordingly.


----------------

update - 19/8/26

Here's what we are going to try, a simple python agent that can launch an interative chat where you can converse with it, it has some tools, an LLM API, MCP client configured that can talk to the MCP server you built, invoke tool calls etc, can store context about chat etc, using something like SuperMemory maybe.

--> building a simple harness related to something about GTM engineering
--> Fine Tuning a base model for writing emails.
--> building a memory layer like SuperMemory of your own.
--> Docker, Kubernetes, Jenkins stuff.
--> can possibly implement a sliding window mechanism in the memory layer.
