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
--> There are a couple of transport methods you can use with MCP servers, one is stdio which will be helpful if you are solely building tools locally, and the second if http in order to share your MCP server with the world, kinda like hosted service.
--> fastmcap CLI can help you with commands to directly invoke tool calls, or you could also use the CLI, TUI from the MCP Inspector. Since we are on a server GUI would not help
--> pip is the official tool in python to get external software modules.
--> Python is classified as an interpreted language because you can directly run the source .py file unlike CPP , JAVA where you first have to compile it to get some executables which you can then run. but python still has a hidden compilation step where it converts the source .py file into a .pyc bytecode to make things faster.
--> When using the chat interfaces provided by the frontier models, the responsibility to manage context is theirs but when you are using their API keys, it's your app's responsibility to manage the context and if its kind of a multi turn conversation, you kinda have to keep on appending messages to keep the context intact. You need to take care of a lot of things when doing this, managing context, cost optimizations, sliding windows etc.
--> OpenAI's SDK is the most adopted dominant standard in the market. SDK is essentially Software Development Kit that OpenAI designed for the developers to use their models effectively. Under the hood, all models communicate using HTTP stuff and you can use the raw network requests as well, it would work fine. OpenAI SDK jusr provides a wrapper on top of it to make things a bit more convenient. Can be used with any inference model.
--> In general, you can just pass along the entire text that you get from the user, and you won't have to manually handle the aspects like tokenization, embeddings etc, model is designed to handle that stuff. In specific cases, you might want to handle the embedding aspects etc
--> import for importing the whole package/module. from .. import .. for importing a specific variable, function etc from that module.
--> OpenAI and AsyncOpenAI are just 2 versions of the same client provided the OpenAI SDK. OpenAI for the synchronous/blocking stuff and AsyncOpenAI for the asynchronous/non-blocking stuff.
--> sys and os are a couple of built in python modules. sys gives you functions and variables tied to the python runtime environment and os gives you a way to interact with the operating system.
--> All of the memory startups in the market are kind of building a memory layer for the AI apps. Basically the model APIs help you with inference, the memory APIs help you with some additional context that can help the model answer effectively. Some examples are Mem0, Letta, Cognee, SuperMemory etc . LLM calls are essentially stateless and they don't know anything about you so what it does is basically time and again it extracts relevant pieces , stores them somewhere in a manner that it is easy to retrieve and then retrieves that data as required.
--> For the memory startups, its essentially just 2 steps tbh. One is read and the second is write. Read is essentially trying to figure out some relevant context from the database to add to the input prompt before the LLM call. Write is essentially figuring out whethere there is some info that could possibly be stored. The read or write could possibly be done after every LLM call technically , but it really depends on the use case. If its like a chatbot, where the messages are back and forth, you would want to do it for each LLM call but if its like an agentic flow where you have asked the agent to let's say perform some task and eventually it spawns a bunch of sub-agents doing sub tasks, there's no point of read/write memory layer after every LLM call as its still refining what has to be done, what's right or wrong and the eventual facts surface only when let's say some checkpoints are reached like a sub task is completed. It makes more sense to add that memory layer there. This seems to make sense for the write, but for read ? what if it wants some context in middle of a sb task ? think about it.
--> Let's talk about the write step in particular . When let's say a sub task finishes or in case of chatbot, LLM responds, the response is immediately shown to the user and at the same time an async call is triggered for the write layer, its another LLM call to maybe a cheaper model where you give it the response you just got plus input that you had sent plus some past messages and the LLM figures out whether there is some relevant info to be stored and can respond with a final JSON. Now the next step you do is reconciliation where you check whether the stuff to be stored given by LLM contradicts with the stuff already present in the memory and add/update/remove things accoridngly. 
--> For the read step considering a simple chatbot example, what happens is let's say you send a message, a LLM call is first used where we pass this message plus previous messages to reformulate the query ( this query is just a more detailed string version of the input message), now this query is embedded into a vector which is then used to compare against the vectors in the db, kind of a similarity search and then you get let's say top k relvant ones, get the plain text for those k vectors and prepend along with the system prompt , current input message and some past messages before triggering the main LLM call of this turn.
--> Now coming to that question of how to decide when the read/write have to be triggered specifically for an agentic workflow. There are 2 approaches here. One is simple orchestration based where you pre decide that read/write needs to happen at start and end of sub task basically. The second approach is agent triggered ( Letta's model ) where the memory is available as a tool call and it is up to agent to use it when needed. This is helpful in scenarios where let's say in the middle of a sub task , the agent is stuck and needs to replan it's course of action, and can invoke memory tool call.
--> One mental model while you are building this stuff. It's good that you are now learning by building but then don't get obsessed about unnecessary details like UI/UX is not right. That is not the motive of this activiy. Motive is to simply just learn the main stuff by building. Optimise for signal to noise ratio.
--> The approaches used by these memory startups include but are not limited to flat vector store, knowledge graph, temporal/bitemporal graph, simple markdown files etc
--> Some things that are ensured while building system prompts by major frontier labs. Telling model specifically what to do instead of what not to do. Putting in few shot examples, telling it specifically what the format of output would look like. Strict hierarchies of authority follow from top to bottom. System prompt being at the top, user prompt being below it. You migt be wondering, how would hierarchies be followed if the model sees everything all at once via self attention. Well these frontier labs use role based control tokens which mark the start, end of system, user prompts etc. Also while doing SFT and RLHF, it is rewarded and penalized accordingly when it obeys or not obeys stuff in the system prompt so eventually it learns to obey stuff in the system prompt. Well we also particularly specify in the system prompt as well that if the system and user prompt contradict, system prompt should take precedence. This is one of the main reasons why frontier labs use XML scaffolding setup instead of plain text while writing the system prompt, because they can have tags like<system_inst> , <user_input> etc which could be used to clearly define authority hierarchies. XML tags are used by Anthropic and mardown headers by folks at Google, OpenAI. By using these tags, headers you can clearly specify key-value pairs denoting rules, exceptions etc . Headers and tags are also high attention boundary markers. During post training, RLHF step etc, frontier models are explicity trained using datasets with delimiters like tags, headers so when the system prompt has those it aligns with what the model is familiar with.
--> Now when you are building AI apps, you don't have control over the system prompt of the forntier model inherently but all of the API docs do provide you with a system message or developer prompt functionality that you can use to specify stuff in the similar format as the model's own system prompt . There's no rule book defined for what tags are allowed so you can invent your own, just make sure they are easy to udnerstand by the LLM.
--> Python is neither pass by value nor pass by reference. It follows a special mechanism called pass by assignment. Whenever you pass an argument to a function, it passes a copy of reference but how it behaves completely depends on whether the object you passed is mutable or immutable. For mutable stuff, the value could possibly change but not at all for the immutable stuff.
--> SQLite is an in-process, serverless, relational database engine. It is built directly into the application process reading and writing to a single cross platform file on the disk. An entire database(including tables, schema, indexes) all stay in one single .sqlite or .db file. Copying, moving files is just a matter of updating that one file.
--> NumPy is a Python library designed for fast numerical computation, especially using multi dimensional arrays. reshape method is used to change the shape of the array without changing the underlying data elements. A simple example is to convert 1D to 2D array.
--> scikit-learn is another python library but it's primary used for machine learning, can help you with cosine-similarity
--> heapq is a module that can help you with heap queue / priority queue algo
--> In python, library is a collection of packages and a package is a collection of modules.
--> asyncio is a library that is used to write concurrent code using async/await syntax
--> ast is a built-in python module that allows you to programmatically traverse, parse, inspect , execute code as structured tree of objects rather than raw text string. it provides a literal_eval() utility that can convert string into whatever python data type it actually represents.
--> Parameterized Query is a way in SQLite to prevent SQL injection possibilities. Basically you leave placeholders and then pass along the value separately while building the query.
--> lists are built in data types in python and are flexible containers and can store any type, arrays need to be explicitly imported and can only store one specific data type
--> json is a python built in module that basically allows you to do json related stuff like serializing json object into string using dumps() or deserializing it using loads()
--> Before Git, Linus's team was allowed to use BitKeeper for free, it was a paid control version system. Someone from Linus's team tried to reverse engineer BitKeeper and BitKeeper revoked the agreement. Linus eventually decided to build a tool for their team and called it Git.
--> There are 4 zones primarily. One is working directory where you write all of your code, second is staging area where you keep stuff like a draft that you would eventually want to check and commit, third is local repo which has the stuff that you commited but its local right now, and the fourth is the remote repository where platforms like GitHub and GitLab come into picture where you can push your local repos so others can access it plus its a way for keeping private repos safely somewhere.
--> git init ( ask git to start tracking your project ), git status ( what's staged, what's untracked etc ), git add ( add the changes to the staging area ), git commit ( to take a permanent snapshot of your staged changes), git log ( will show you all the commits etc)
--> git branch ( to make a new branch ) , git checkout ( for switching to a different branch ), git merge ( for merging the branch ) , branching is an interesting concept where let's say you have your main branch and you want to add a feature let's say so you can make a feature branch separately , do your stuff and finally create a pull request to get your changes pulled in the main branch for eg. Now when you are trying to merge this, you might end up with a bunch of merge conflicts which you will have to either resolve via CLI or a GUI etc
--> main and master branch technically just represent the same thing. Its just the industry standard that now commonly uses main branch to disassociate from negative historical references. Whenever you create a new repo, you generally see this command, "git branch -M main", which changes the master's name to main.
--> git remote add origin ( to connect to a remote repo ), git push origin main ( push code to github ) , git pull origin main ( to pull latest stuff from the repo, does the fetch and merge at the same time), git clone ( to clone the entire repo in local)
--> GitHub vs GitLab vs BitBucket ? GitHub is best for open source collaborations, community first approach and its like the social network for developers. In GitHub we have Github Actions for CI/CD , but its supported by a bunch of external plugins made by the members in the community . GitLab has built in DevOps and deployments are native features and the CI/CD pipeline infra that they have built is like the best in class , most mature, standardized, robust etc. Can run GitLab on own private servers using their community editions. BitBucket is primarily like a VCS designed for teams who are locked into the Atlassian ecosystem
--> Docker creates containers and Kubernetes orchestrates and manages them. Basically you write code and package that up into a docker container. To be precise, you write a docker file that contains all of the dependencies etc, that docker file builds a static immutable image containing the code and the environment specifications and then you execute this image to get the docker container. You eventually have those docker containers running across a bunch of your servers and all of these containers are then managed by Kubernetes ( scaling, networking, ensuring they are healthy). The docker file is shared along with the application code, its pushed to github/ gitab / other VCS and the developers can just pull it , use the docker file to build the image and then execute it to get the docker container running on their system. Another way is that for testing, deployment etc, other devs don't have to build everything from scratch, what they can do is just buuild the docker file ( docker build ) to make the image and push that image ( docker push ) to a container registry like Docker Hub, Amazon ECR, Google Artifact Registry. Other devs don't even need the docker file or  the entire code locally, they can just pull it from the container registry and run it on their machine ( docker run ....) ( that just pulls and spins it up automatically)
--> docker container is fundamentally just a bunch of processes running on the host server and not the full virtual machine. To the other processes on the server, it would feel like its just some other process but the containerized app thinks its running on its own isolated machine with own file system, network, process space etc. 
--> docker image isn't a single file but its a directory consisting of multiple layers stacked on top of each other. When pushing or pulling the image to/from registry its transferred as a tar ball (.tar.gz), with a JSON file showing how those layers fit together.
--> Kubernetes is an automated system that is designed to maintain a desired state across a group of servers ( a cluster). Kubernetes cluster fundamentally is just a bunch of servers which collectively make one single massive machine. They pool all their resources like CPU, RAM, disk space etc and then cluster as a whole manages what has to be done with those resources (its not like resources of one machine can be used by other but they don't individually control what happen with their resources. It's the cluster that controls it). When you wanna deploy a new app, you don't send it to a specific server, you just send it tke kubernetes cluster and then the cluster decides which server has the room to run it. These individual servers are called nodes. The cluster fundamentally divides the servers into a couple of sets. One set becomes the set of manager servers who don't run the user facing apps and their whole responsibility is to basically manage things, API requests, ensuring stuff is health, managing traffic etc, another set is the worker nodes that actually do the heavy lifting . Each worker node has a container engine ( like Docker ) to run the pods and a k8s agent ( kubelet ) that receives orders from the brain ( the manager servers ). It seems like a master slave architecture.
--> Pod is essentially the smallest deployable unit . Pod can contain some docker containers that need to run on the same machne. There can be multiple pods on the same machine. Containers of the same pod share the same network (IP) and storage volumes. ReplicaSet is like the scal engine. It ensures that any given time a specific number of identical pods are up and running on the system. If pods crash, it can spin up the replacement and so on.
--> Deployment is the lifecycle manager. You rarely manage the pod or replicaset directly instead you declare Deployment and the deployment ensures zero downtime using things like ReplicaSet etc. Then there is a deployment controller that continuously checks the deployment you declared and kind of takes a diff of current state vs the desired state and if they don't match, it does stuff to reach the desired state.
--> The local kubelet agent on each of the worker node also keeps a check on the health of that node and let's say if some pods crash or are in deadlock, it restarts them again based on the restart policy. If the entire server let's say dies, the node and the pods etc running in it are marked as dead and fresh pods are started elsewhere in the cluster.
--> K8s also balances traffic based on the master-slave architecture itself. HPA ( Horizonal Pod Autoscaler ) scales in/out basically increases or decreases the number of pods as per needed. VPA ( Vertical Pod Autoscaler ) scales up/down basically increased or decreased the capacity of pods ( CPU/RAM/disk etc) as per needed.

21/8/2026 -->

--> Terminal is basically a program that you can use to interact with a shell like powershell, you can use these shell commands to interact with the underlying operating system. Shell examples are powershell, bash , csh etc
--> WezTerm seems to be a good upgrade when it comes to terminal. It almost has all of the capabilities of simple windows terminal plus some additional. The reason why I am shifting to it is because it can preview images etc when I am working with coding agents. Currently I am using Pi agent and in order for me to preview images, I need WezTerm, normal terminal won't allow that.
--> WezTerm supports Kitty Graphics Protocol that allows you applications to send the imaged data and it can do the inline rendering of those images in the terminal.
--> I have also setup SSHFS Win Manager so that I can mount my hetzner vps's file system ( basically a screenshots directory) locally and automatically save screenshots there and then can directly access it on the server 
--> Historically, terminal used to be an actual physical device separate from the main computer and you would talk to terminal and then the terminal would communicate with the main computer. Now, there's no terminal really but it's the terminal emulator actually, acts like a terminal but there's no separate devices. In modern terms, we just use terminal and terminal emulator interchangebly so WezTerm, Windows Terminal all of them are just terminal emulators essentially.
--> TTY (originally comes from teletypewriter) is a terminal device/interface through which a program can interact with an interactive user. When you run 'tty' on a linux setup, it tells you that your current shell is attached to a particular terminal device. the concept was introduced as an abstraction by UNIX because they didn't want bash to worry about which terminal device its connected to so UNIX gave BASH a standardized TTY interface. So a terminal device talking to TTY talking to the shell historically.
--> PTY is pseudo terminal. Its a software implementation of an actual terminal interface. It's pseudo because in a PTY setup, its a terminal emulator ( not a physical terminal ) that talks to PTY which then talks to the shell. It has a master-slave setup. PTY master talks to the terminal emulator and PTY slave talks to the shell.
--> TTY is the OG and PTY is an extended version of it.
--> PuTTY is essentially just a software that allows you to connect to the remote servers using SSH that's it.

--> Blindly using MCPs for every little thing is kind of a dumb decision. Mario Zechner has written a bit about it at https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/. Whether you should use it or not is conditional. Let's say you are doing frontend stuff and you want to provide a way for model to look at the UI take screenshots etc and fix stuff, rather than blindly using playwright MCP or dev tools MCP , you can simply write a simple script that does that and avoid context bloat of giving your agent unnecessary context of all the tools in the playwright MCP etc. For use cases where its related to data like the Clay , Apollo, HubSpot MCP built on top of APIs, you can use them rather than building it from scratch by scoping the toolset. Well you can build all of it yourself but in some cases it would be waste of time.

--> Claude skills are essentially just markdown files where you can write insights about how an expert in a specific skill would deal with a problem statement because the SOTA models are still general purpose ai and need specific expert guidance and dealing with specific tasks.

--> Claude.md is basically a repository or entire project level markdown file where you explicitly tell it the exact DOs and DONTs and other important things about the projects. SKILL.md is another markdown file but it's skill/task specific and used when the actual prompt aligns with the need of that skill. The Claude.md is basically injected with every prompt sent to the LLM so it might feel like it bloats the context window but then Anthropic uses Prompt caching so that it doesn't process it again and again. Then there is SKILL.md which is only used on-demand maybe what the skill does is indexed but the entire skill is not pulled in each command.

--> Pi gives you more control over what exactly is happening internally in the harness and gives an opportunity to actually learn about internals etc and customise as per need whereas Claude Code Agent is like an out of the box agent for people who just want to simply use it.

--> Pi doesn't support using sub agents natively. Its just one main agent. Claude Code has that feature inherently where the main agent the user is talking to can spin up sub agents for doing specific tasks. This is needed to solve the context window issue so that the main agent's context window doesn't get bloated with all the context. Some sub agents are in-built but you can also define your own sub agents as well, plus model etc they can use. The sub agents don't talk to each other, they talk to the main agent only.

--> There is also a concept of Claude Code Agent teams, where the main agent can make a shared task list and spin up a bunch of sub agents that pick stuff from shared list and mark it as finished and in this case the aub agents can also communicate with one another. This is experimental.

--> Claude Code Sub agents are considerably better as compared to Agent teams and Agent teams is still experimental (https://www.youtube.com/watch?v=jT1rg3TBf-I)

--> Terminal-bench ( tbench.ai ) --> benchmark for AI agents in terminal environments
--> swe bench tells you the ranking of actual models based on capabilities, it contains open weight models as well . You can filter by agent which basically means the environment in which the benchmarkign was done. It might not be up to date so it's best to check multiple benchmark platforms. Also, a model being some points higher or lower doesn't necessarily make it bad overall, its just an idea. Also, don't blindly rely on ranking, other factors are also there which need to be considered like the context window. A good mental model is that if a model is present in the leadboard and is decent enough, it's good, plus the cost shouldn't be drastically high.
--> Claude Code agent harness can be used with any model, there are ways to get around with it using LiteLLM

--> For the Pi vs Claude Code Agent, I feel Claude Code should be the go to choice for any non techie who just wants to get started with using agents but Pi should be the go to choice for the cracked ones who want full control over what's happening.

--> Sub-agents are essentially just markdown files containing YAML code denoting what the sub-agent is, description, tools, model etc and then the entire body of insights related to that specific sub agent. description should be really precise as that is what decides whether the sub agent is spun up by the main agent. There's a concept of progressive disclosure that means the entire body text of each sub-agent isn't read, its just that the main agent goes through all of the sub-agents, reads only the meta data to first decide whether it needs to use this specific sub-agent or not and only then the body text etc comes into picture.

--> How to write a greate sub-agent ? The description should be really precise as to when it has to be used, words like "Use Proactively", the best model that would perfectly solve that, then comes the body, which is the whole brain. The body can basically point to specific skill that you want it to use as well.

--> The mental model that you need to have is that you need to break down your entire big system into many bits and pieces, also called sub tasks and these sub tasks should be done by sub agents who are specialists in that specific domain basically. A frontend task can primarily be broken down into different steps , each can be done by separate sub-agents.

--> Even if the sub-tasks aren't exactly parallel, you should still consider using sub-agents because it might not save you time but it will end up saving you money ( because you can tweak what models you use for specific sub tasks) plus you can also keep the context of the main agent short , precise and not bloated.

--> One important thing related to the entire sub agents thing is that you need to figure out a way to store intermediate results at checkpoints ( these checkpoints need to be hard coded in the body of the sub agent markdown files itself )

--------------------------------

--> update - 24/8/2026 , VPS killed a tmux session that had a pi session going in it that was apparently doing a build that reached around 5 GB and it fucked up the entire frontend pipeline in the middle. It was an OOM kill, the system ran out of memory.

Some possible solutions were suggested, swap, zram , cap the max heap for node build, I need to figure all of these things out right now and fix the VPS.

Analyzed the memory via free -h, tells you about the available RAM, after postpone stuff looked fine, also checked htop and stuff was fine, main issue was that build, and at that time, I also had 3 other pi sessions running as well that were consuming 250+ MB each , plus the VS code server running, 500Mb-1GB, then there's python processes around th e linkedin warmup.... we eventually ran out memory , that's the core of it and we don't have money to rescale servers at every single point. What are we gonna do ?

Recovery --> Figure out if there's a way to get that pi session back where we were building the frontend pipeline or else we'll have to start from scratch, ffs!

Options to fix this issue without spending money -->

1. Use pi sessions wisely, had a bunch of sessions running, each of them consuming some memory. 
2. experimental.cpu , --max-old-space
3. Swapping
4. zram, sda, QEMU disk

Learnings -->

--> Pi is a Node CLI, every single terminal you open a new session it gets its own node process. ( its a command line interfact to talk to the Pi agent, and every command you type is just handled by the JS code under the hood.)
--> Need the VS code server, not so comfortable with vi at the moment tbh . Need those python processes running in the background for the linkedin stuff as well.
--> So javascript is a programming language, which was historically, purely an interpreted language but now it's kind of a hybrid approach and is JIT compilation. Just In Time compilation basically means right when the code runs, the profiler figures out the hot paths and converts them into native machine code, but it isn't compiled way ahead of time like classic CPP or JAVA.
--> Browsers run the JS and that's how they basically render web pages with JS in it.
--> Someone took JS out of the browser engine and made Node that is JS runtime outside of browser where you can directly write and run the JS code and you don't need the browser engine. 
--> V8 is the actual javascript engine inside Node that parses and executes the javascript code at lowest level.
--> npm comprises 2 things ( one is registry that is a giant hub of a bunch of javascript libraries hosted by developers across the world and the other is cli tool using which you can pull packages from this registry). There is something called pnpm that solves a problem. If you have multiple projects on a server and you run npm , it will get the packages/libraries for all of the projects separately bloating up stuff. pnpm solves this where it basically gets it at a common place in disk and then projects sort of create symlinks to it if they want to use it.yarn is an alternative for pnpm with same idea but different implementations. All of them pull stuff from the same registry essentially.
--> there's package.json that contains meta data about your project, stuff like name, dependencies , scripts etc
--> package_lock.json helps you solve the problem of "it works on my machine" by locking the exact version of every single package in the entire dependency tree, plus a hash to verify the integrity. auto generated, shouldn't edit . pnpm equivalent is pnpm lock.yaml etc
--> CSS is Cascading style sheets, a language that helps you make the HTML content look better.
--> Tailwind CSS is a CSS framework which provides components and utilities as a wrapper over raw CSS to give you a bit of flexibility to avoid wriitng raw .css files.
--> Shadcn UI just gives you a collection of UI toolkit built on top of ( Tailwind CSS styling + Radix UI unstyled components )
--> framework vs library vs package ?
--> React is Javascript library used for building UI components for your frontend applications. Next.Js is React framework that wraps up React along with the missin infra like ( API endpoints, Routing, rendering strategies )
--> npx is a command line tool that allows you to run a package from the npm registry, unline npm command line tool where you have to first install it and only then you can use it.
--> After writing Next.JS application, your app contains a bunch of fancy extensions files right but the browser can't understand it directly, so you need to build the app which basically means you need to a bunch of steps like transpilation, resolving imports etc to get .next/ directory which contains a bunch of structured files ( HTML, CSS, JAVA ) this time and when you run your app, what happens is it creates a Node JS process that reads and executes your code, starts a server and starts listening for requests at a specific port, and routes the requests to the correct code in the .next/ 
--> When you write the source code of your Next.JS app along with the creatives, it sits in the disk ( could be of your laptop or the server ), now when you build the code, the build output again stays on the disk, now when you run the code, Node process is created by OS, this Node process reads and loads files from the .next/ into the RAM as and when needed. It also opens a network socket and starts listening to a specific port for incoming requests. When the requests come, it routes them to write code that handles it, can load more stuff from disk into memory, computes a response (CPU involved) and sends it over to the network.

-->During the build of the Next.JS app, Node is what primarily does all those steps we discussed and anything Node does will require RAM. Also, builds are more hungry for RAM as compared to the actual run of the NextJS app. During build, it has to hold a bunch of step in memory simultaneously as compared to when the run happens.

--> Node's core execution model is singe threaded ( one event loop thread running your code ) but it does support genuine multithreading using worker threads as well.

--> Next.Js has webpack/turbopack that it uses in the build process as a bundler. During the build process, the bundler starts from entry files, starts converting them into core js files and then bundles them into small number of optimised compiled files. Now this task of compiling so many files is highly CPU intensive so it breaks the task down and spawns a bunch of individual Node processes each running on a different CPU core simultaneously. Each of these Node processes will have their own V8 instance, heap so there's a property called experimental.cpus that allow you to limit the no of Node processes the WebPack can spawn during the building task, kills parallelism essentially, build will become a bit slow but lower total RAM used at a moment. Each of these Node processes, have their own V8 engine instance and their own memor model. old space is essentially the heap part where the long lived objects are and it can grow to a considerably huge extent because it isn't capped by default, it can just grow to the amount available, now this can capped using --max-old-space property.

--> Swapping is a technique in OS which gives you an illusion that you have more RAM but technically you don't. What happens is that when you run out of RAM, the OS kernel figures out the least used pages ( small chunks of memory ) and moves them to the disk ( swapping out ), this frees up some RAM for other processes to use, when the pages on the disk are needed again, they are swapped back in. The issue with this, is swapping out and in from disk is kind of a slow process. If you are at your memory limit and let's say a lot of swapping happens, your system will end up spending more time swapping pages to/from disk, and less on the actual work. This is what is called thrashing and make the server feel like its completely frozen. PLus I am also using VPS, which means the disk that I have is virtual disk made available with the help of virtualization on top of common physical hardware and so it is made available to a lot of people, its QEMU disk, ( QEMU is virtualization software ), so it will make the swapping process even slower.

--> swappiness is essentially a property to denote how hungry the system is for swapping stuff.

--> zram is a way for you to use the concept of swapping but without moving data back and forth from disk , you essentially reserve some memory from the RAM itself for zram. and the least used stuff is basically compressed and moved to zram . back and forth happens with zram instead of disk this time and it is fast.

----------------

28/8/26 ( 18:05 ) -->

Understanding backend from the first principles -->

Request is sent from frontend to backend on an app, basically from client to server.
This server is essentially a machine designed to receive and handle that request. Anything and everything that happens right after receiving this request to finally doing all of the stuff and sending some response back to the frontend is what is collectively called the backend .

Now, in order to configure a machine to behave like a server and handle, process requests and do other stuff, we need to write some code using backend programming languages like JS, Java, Python etc. Natively writing a lot of code using these languages is a bit painful as you'll have to write a lot of code so essentially we have frameworks and package managers. Frameworks are like wrappers on top of the native backend programming languages along with some other utilities, and we have frameworks like Express, Django , Spring etc. We also have package managers, where there's a common registry where people publish packages ( basically useful utilities others can use) and the other devs can install those utilities from that registry. 

Now in order to store the data, we need database, and our backend server talks to this database for read/write/delete stuff. Most famous options being PostGreSQL, MySQL and MongoDB. Fundamentally that is all you need for the backend part, a server and a database. 

In your backend server, you basically have different routes configured and they collectively build the backend API, these are essentially just different routes with different implementations designed to handle different types of requests sent from the frontend. The API can use different naming conventions like REST, GraphQL etc

Then we have the infrastructure. This basically means we have 2 options, either we buy the machines or we rent it. There's no point of buying such machines for your vibe coding ideas right so we rent it, this is essentially what cloud computing means. Big giants like GCP, Azure or AWS have data centres where they have these big physical machines and then they use virtualization on top of it using hypervisors to give you some VMs ( Virtual machines ) out of the box with different compute capacity packaged as different pricing plans basis a subscription model. You rent these VMs and essentially host your app on thse VMs. THis is IAAS.

Now there can be cases, when you are scaling and your site needs to handle a lot of load of traffic so in that case you can provision more VMs etc and then have a separate VM and configure it to behave like a load balancer and you can basically scale the VMs horizontally and vertically as and when you need. 

Now setting up all of this stuff isn't easy so the big tech giants also provide you solutions like App Service where its their responsibility complete to scale the servers, load balancing and stuff like that and you won't have to worry about it. This is called PAAS.

The concept of microservices comes from the fact that a single backend and eventually grow up to become very bulky and hard to maintain and reason to about it so the wise choice becomes to split it up into multiple backends and each of them could have their own load balancers, db and stuff and they collectively are called microservices that handle specific tasks . eg- payment backend etc, the best part is that this way, different microservices could be using different tech stack etc as well.

Now these microservices that do some specific task are also abstracted and there are companies out there that handle your payments etc , these are called SAAS platforms 

There are other additional technologies as well that might be needed later when you grow like caching layer, Job queues etc.

Then there's BAAS. Backend As A Service, they can just handle the entire backend for you. ( Server, DB, Auth systems, API). Examples are Supabase, Firebase, Convex, Appwrite

Convex seems to be the best overall. I have used Supabase in the past and convex is much better both price and capabilities wise. it also helps a lot in the agent development because every little thing can be configured in the code itself and dashboard configs aren't necessarily needed, this is helpful especially for agents since they can see all of it in the code.

Convex has some crazy fetures. One is reactive queries, no manual wiring. We have query functions written in typescript that basically get some data from some table in DB, and it's showed in UI let's say. Now this data could be updated right, in most cases, you need to manually re fetch that data via polling or set up web sockets etc but in this case, Convex automatically checks which query functions touched this data and automatically updates the data for every client who subscribed to that query automatically. Backend logic is just typescript functions, no ORM as such. It's natively built for realtime apps like chat apps, dashboards, collaborative tools etc.

Convex has queries, mutations, and actions. Queries is for reading stuff from database, mutations is for writing to DB, and actions is for calling third party service APIs. We also have a schema.ts file to defined the structure of database.

Convex provides server functions + database, managed as a cloud service. Convex runs it on their servers, store data and basically keeps data synced in your app. 

What happens is that in the convex/ folder in your app you define the schema.ts and the functiins ( query, mutations and actions) . Then in the core frontend code that you own, you basically invoke function calls to these functions you defined in the convex/ . When you use something like "npx convex dev", it essentially helps you in authenticating then binding a project ( that you created on the convex dashboard) to the Next.js app, it then starts a watcher which tracks whatever edits are done in convex/ and sends those updates to the dev deployment of convex, essentially to convex servers and when you invoke function calls using convex client, it basically sends those function calls to the convex server and returns the results .

convex deployment here essentially means it's a single instance of backend with its own functions, DB and env variables etc.

------------------------------------------------------------

For OkGTM project, why did we pick Next.JS and not Vite or React.

Vite is a build tool for modern development. It's the engine that runs behind the scenes when you are coding your app and packages everything up for production.

It works in 2 ways,
-> When you are actively developing, and doing changes in different files, Vite serves updates to the browser for those files almost instantly however the older tools took time . This is because older tools had to bundle up your entire app before the updates could be shown but for Vite the pages are served individually to the browser on demand basically using a feature browsers support natively called ES modules.

--> For production, it switches to a bundler where it combines and minifies all your code into optimized files - smaller, faster, ready to deploy.

People primarily use it because it gives you fast dev server even for large codebases.

Is it related to WebPack or Turbopack?
Vite, Webpack and Turbopack , all are JS build tools , bundlers with different set of trade offs. Webpack is the older, more matured one but it's historically known for it's slowness and Vite was made as a response to that and now we have Turbopack made by Next.js made specifically to replace Webpack in Next.js

Vite was designed originally to work with Vue but then plugins were made to make it work with React etc as well. There could be a way to use Vite with Next.js as well using some plugins etc but the Vercel team wanted to come up with something unified ( not using separates dtuff for dev and prod builds ) plus they wanted to experiment with Rust as a programming language for build tools ( Webpack and Vite are JS based) for performance reasons.

--> ES Modules (ESM) is a JS built in feature, that allows code to be split up into multiple different files that can import from and export to each other. Vite leverages this for the fast updates where it only serves individual files to the browser on demand. Before ESM, browsers had no way to figure out what file depends on what so the blunders like Webpack had to stick everything together and send it all to the browser as one bulky js file. 

In order to decide whether the frontend stack needs to be React or Next.js. The best way is to ask whether strangers need to find your website via the google search ? does fast loading of the page matter when the person lands ? Is there a CMS driven layer like the blog ? --> Answer is Next.js

If the entire product is behind a login, internal tool, admin panel, dashboard, people find you via Google doesn't really matter etc --> React is the choice. 

If its hybrid and you have both blogs for SEO and core SAAS behind login as well --> then too you should go for Next.js . Mainly if SEO is a priority, go for Next.js

Next.js is super important for SEO and solves the problem that React faces. With React, the server sends the javascript file that's it no content initially. The browser needs to download the js files and then build DOM using it. Google's crawler can still execute javacript these days, but there are caveats, heavy JS pages can take times and might be skipped, plus time to first content matters for a real person coming on the page and that is exactly what the crawlers use as well as one of the metrics to figure out whether to rank the page or not. 

Next.js basically renders the page's HTML on the browser itself so what gets sent to the browser isn't empty stuff, it's actually the HTML content, and then React hydrates the HTML content( attaches interactivity) in the browser but the crawler can see the content alredy and time to first content is minimal and the entire JS execution pipeline isn't needed before you can see the content. 

The core mechanisms of Next.js that help in SEO are Server side rendering, Static Site Generation, Incremental Static Regeneration, Built in meta data handling, Automatic code-splitting per route, sitemap and robots.txt generation.

-----------------------------------------------------------

In general, REST and RESTful API are just used interchangeably but if we were to get too technical,

REST ( Representational State Transfer ) is just an architectural style designed by someone that should follow some principles in theory. These are -->

--> client - server concept ( client sends requests and the server handles them)
--> Server doesn't maintain state between different requests ( each request contains all of the info needed to denote the state)
--> the request contains the URI, JSON with data that might be involved in resource manipulation, type of request etc 
--> HATEOAS ( Hypermedia As engine of application state) ( Response can contain links telling users, what they can do next)

and others. Now the people adopted this structure loosely ( not following everything strictly ) and end up calling it RESTful APIs

--------------------------------

Relational databases fundamentally mean that the data lives in tables (rows and columns) and relationships in data is defined by references between tables.
Non relational databases comprises all sorts of databases that don't use the traditional tables storing the data logic. It comprises document stores, key value stores, wide column stores, graph databses.

Relational databases like Postgres, MySQL etc become the go to choice when you know that your data has some relationships, schema won't change much basically, you need complex queries etc.

Non relational databases make sense, when the structure or schema isn't fixed and would change frequently in early development so you don't want migrating issues etc. You need to access data primarily as self contained chunks, and won't need a bunch of joins etc, plus the attributes of different records in the same table vary ( like different products could have different attributes in the same table)

Most of the SAAS, agencies etc are good with relational databases itself specifically Postgres because Postgres now handles JSON very well, in most cases you will end up with relationships between data even when at start you don't think of it and then you'll have to simulate the joins thing in the code if you go ahead with the non relational thing which is worse than the db doing it . Postgres should be the go to choice unless you have a very specific reason not to go ahead with it.

The above is dev phase, for deploying the convex backend to prod, you essentially use "npx convex deploy", it moves the functions, schema.ts etc there to a prod convex server, gives you a different deployment link which your Next.js app has to then point to, and you also need to setup envs separately for prod. Also, the db in prod starts from a clean state but you can import and export stuff between deployments.

In Convex, we have the concept of internal functions and public functions. Internal functions are defined with internalQuery, internalMutation, internalAction and the public functions are defined with query, mutation and action. 

There's also a concept of Cloud URL and HTTP Actions URL. Convex Cloud URL is essentially just the deployment URL that the convex client talks to for the normal convex functionalities whereas the HTTP actions URL is deployment site URL that is used with HTTP actions, a functionality in Convex that is used to expose HTTP endpoints that other external services can use and post to . This is needed in case where they want to send some response to Convex, but they don't speak the language of Convex so they just need simple HTTP endpoints to post to.

-------------------------

Figuring out the DNS stuff -->

Bought the domain on hostinger. You registered the domain essentially and hostinger is your domain registrar and not necessarily where your app lives. Using Vercel for hosting the app because hostinger's hosting is paid and Vercel offers a really generous free tier . Hosting here essentially means that your app essentially is hosted on Vercel's servers which means any requests that are sent to okgtm.com ( people typing that in the browser) will be sent to Vercel's servers and Vercel will serve them with stuff.

Domain and hosting are fundamentally decoupled in that sense. You essentially need a way to tell the internet that when someone types okgtm.com, send them to vercel's servers where your app is hosted. That is what DNS does.

DNS is Domain Name System. DNS translates the human readabale domain names into machine understandable info ( IP address, or instructions about how and where to route traffic)

DNS records are entries that live in your domain's DNS zone. Common ones that you'll deal with are
--> A record, maps root domain to an IP address
--> CNAME record, points sub domain to another host name
and others

DNS provider is the company/service that is responsible for hosting your DNS records and answering the quesiton of what does a specific domain or subdomain etc point to. it runs the servers that hosts these records.

The nameservers are the actual servers ( hostnames ) that actually answer your domain related DNS resolution questions. By default, the registrar is the DNS provider as well but you can change that to use some other DNS provider like Vercel by pointing the nameservers against your domain to the Vercel's nameservers and then all of the DNS records you can manage in the Vercel's dashboard itself.

For okgtm.com, I am just changing the nameservers to point to Vercel now.

A DNS record primarily contains, 
Name (sub domain ? or @ if root), Type , Value ( hostname ?), TTL, Priority.

TTL is Time To Live. It means how long ther DNS servers across the world are allowed to cache this DNS record before they have to re check.
A type record points to an IP address itself.
CNAME type record points to another domain name and tells to resolve whatever that domain name resolves to. It's canonical name

Priority field of the DNS record is used particularly for the MX type records for prioritizing which mail server handles the request when multiple mail servers are configured for the same domain.

like okgtm.com served via A record, www.okgtm.com served via CNAME record .

For labs.okgtm.com --> just add that DNS record, then add that domain in the settings-> domains of the project as well and done.

-----------------------------------------------------------

Setting up emails for a domain -->

Setting up the business email ujval@okgtm.com --> Zoho mail's plan is much better and offers more features for less price compared to hostinger mail. I made a mistake here. No issues, from next month, we'll pick Zoho mail. Canceled the auto renewal.

Now Vercel is my DNS provider, it's servers are where the DNS zone is so I need to configure some more DNS records ( MX, TXT, CNAME etc) there for setting up the mailbox of ujval@okgtm.com. The mailbox provider right now is Hostinger and it asked me to add a bunch of DNS records specifically for enabling the mailbox and these included MX, DMARC, TXT etc type records.

How does this entire thing work, fundamentally ?

Setting up the emails for a domain involves 2 directions configured separately ->
One is receiving email and another is sending email. Receiving email is essentially that when the email is sent to ujval@okgtm.com where does it actually land ?
Another is sending email, when the email is sent from ujval@okgtm.com, which server actually sends it, how does the receivers know that it's not fake from a spoofer etc ?

Email provider is the service like ( Hostinger Email, Zoho mail etc) that helps you configure a mailbox for your domain. These providers essentially give you some storage for your email plus a login. The email providers have the mail servers running which you can then use to send or receive emails.

MX records ( Mail Exchange) are DNS records that basically say, "for this specific domain, the emails should be sent to a specific mail server" so someone sending email to ujval@okgtm.com, the process would look like, look up the MX records and check which are the servers that are handling this specific email, and choose to send it to the highest priority one ( the one with lowest no.) . In your case, hostinger mail, gave you MX records that you added in the DNS zone of Vercel, and its values denotes the hostinger's mail servers.

This is kinda similar to what happens when someone types the domain name and the traffic is routed to vercel but in this case, its about mail delivery. 

IMAP/SMTP --> How your devices talk to the mailbox. These are 2 different protocols for 2 different tasks.

IMAP ( Incoming Mail Server ) --> protocol basically helps the phone/email client to read/sync messages from your hostinger's mailbox. imap.hostinger.com is Hostinger's mail server and you basically authenticate as ujval@okgtm.com to get the messages from it's inbox.
SMTP ( Outgoing Mail Server )--> protocol used to send messages. When you send an email from the phone/email client like GMail after you have authenticated as ujval@okgtm.com with smtp.hostinger.com ( this essentially is Hostinger's outgoing email server) , your email basically goes through this server to the recipient/s.

Essentially, when you add ujval@okgtm.com as a non GMAIL account in Gmail app, you are telling Gmail to use IMAP at imap.hostinger.com and SMTP at smtp.hostinger.com

Autodiscover and Autoconfig are special DNS records basically using which when you are connecting the hostinger mail with email clients you don't have to manuakky type in the IMAP/SMTP host servers etc, it automatically figures that out once you authenticate with the mail and pass.

Alias ---> Extra mail ids that basically deliver stuff to the same mailbox, mails sent to ujval@okgtm.com, support@okgtm.com etc are land into one common inbox, ujval@okgtm.com
Forwarder --> Mail sent to this address gets forwarded to a different external address. Eg Mail lands in contact@okgtm.com, forwarded to contactujval@gmail.com. You don't need to have a dedicated mailbox for contact@okgtm.com with Hostinger for this. The concept is different from what happens when Gmail client connects to imap.hostinger.com. In that case, the mails actualy stay on the hostinger's server, and dedicared mailbox and you just get a sync of email messages. In the case of Forwarder, the mails are simply redirected, they don't stay on hostinger's servers.

Resend is a programmatic email sending service and we need to basically add specific DNS records to tell to the world that ujval@okgtm.com actually authorised Resend to send emails etc

------------------------------------------------------------

30/8/26 (12:34)

Understanding the security aspects of a webapp fundamentally

--> Authentication and Authorization, authentication is basically, confirming identity ( who are you ? login , biometrics, password checks etc), authorisation is different access levels for a user ( What are you allowed to do ?). You can basically build your own authorisation and authentication system but it's much better that you use third party services like Firebase, Auth0 or Clerk etc because they really take care of every little detail which you might miss. Let users sign in using their Google, Github accounts etc, this way you can leverage the security infra of these big players. 

The auth system touches a lot of pillars like session/token management, email verification, MFA etc and each of them has decades of accumulated attack patterns so there are a lot of ways in which this can go wrong. It's hard to maintain such an auth system yourself so it's much better to delegate this stuff to someone who's an expert at this.

--> Define clear role based controls for authorisation and assign permissions to each role properly. Always ensure checks on both client and server side for permissions, never trust the client side checks alone.

Authorisation comes into picture after authentication. 

--> Data Security --> Ensuring the data remains secure in the entire lifecycle starting from when it enters your system right till it lesves the system or is deleted. Think about it in 3 layers, data in transit, in rest and in use. Each of them requires different measures.

For the data in transit, always use HTTPS. You get the SSL certificate, and then the data moving between the client and server is essentially encrypted and anyone trying to intercept the network traffic like public wifis, compromised routers etc can only see cipher text.
This is generally sufficient but if the data is like really sensitive, you can use application level encryption as well, you use strong encyrption and never hardcode encryption keys, always use env variables. Ensure that .gitignore rightly ignores all sensitive stuff etc as well. The env variables should be present in the platform's secret manager and not the repo.

Unencrypted data at rest is also risky if someone somehow gets access to the disk or db so most managed services like Convex ensure the data at rest is also encrypted.

When the data is in use, being actively processed in memory, the risks are, the memory might be dumped to a log file which contains password etc, or logging / error tracking tools accidentally printing sensitive fields. The way to fix this is to not log entire request bodies and ensure that the sensitive fields are redacted and for error tracking tools , ensure that sensitive stuff is scrubed before the stack trace is dumped etc.

Next is data validation, whenever some data enters the system, could be through user input, always ensure that it is validated and never trust the user. checks like invalid email format, password level checks etc. Never trust the client, all of these checks should also be present at the server level. This applies to file uploads etc as well.

For file upload validation specifically, enfore file size limits, check the type of file using actual signature/magic bytes rather than relying on the extension type or content type in header. Store uploads somewhere that doesn't execute code, it could be a malicious script disguised as an image and might trick the server into executing it. Also scan for malware if you are accepting uploads from public users at scale.

Attack Prevention --> Protecting against stuff like Cross Site Scripting (XSS), SQL injection or Cross Site Request Forgery (CSRF).
XSS happens when the attacker injects malicious code in your web page. You should sanitize input and stuff before displaying it. Use content security policy headers to implement an extra layer of protection. Let's say the hacker types in a comment and you just dump that comment in the html of the web page, it could be some malicious code that now gets executed on other user's browsers. 

What you should so is basically escape that input which means converting the characters that hold special meaning in HTML into a form that appears same visually but after converting, the browser's parser knows that it isn't markup. something like < is converted to &lt etc.. Most modern frameworks like React, Vue etc do this automatically when you render variables normally.
You should also have content security policy headers in place. These tell the browser to only execute scripts from trusted allowed origins so even if someone mailiciously injects script tags with src pointing to their website and you didn't escape characters, it won't be executed because it isn't a trusted origin.

SQL injection is basically when the hacker tries to breach the guard rails by passing in input executable SQL syntax thinking that in backend, we could just concatenate the input, if we do that, his SQL syntax can get executed which is not good. What you should be doing instead is, use parameterized queries in which case, the input is never treated as SQL syntax, the actual query is compiled and parsed first in DB with input still as placeholders initially and only after that the input is used for filtering and stuff so it won't get executed as SQL syntax. 

You can also use ORM's like Prisma or Drizzle etc in which case you won't have to worry about this as it's their responsibility of building parameterized queries under the hood.

CSRF ( Cross Site Request Forgery ) happens when a malicious site tricks a logged in user's browser to make an unwanted request to your site using their existing sessions/cookies. The way to fix this is CSRF tokens and SameSite=Strict . In CSRF tokens method, the server generates a CSRF token as a hidden input field when you are submitting a form let's say, and when you hit submit, the token is validated against what was generated by server. A forged request from other site doesn't have any way to figure out this token because of same origin policy. Another method is SameSite=Strict property of cookies, in which case browser won't allow forged cross site requests with that cookie.

Same origin policy is a strict browser rule that fundamentally means that a web page running javascript from one origin cannot read or intereact with the data from some other origin unless explicity allowed. What counts as the same origin ?

--> Scheme ( HTTP vs HTTPS )
--> Port Number
--> Host name

All 3 must match for it to be same origin.

CORS ( Cross Origin Resource Sharing ) is a mechanism by which a server can deliberately relax the same origin policy for specific cases. This is how legit cross origin requests are made like the frontend of your app hosted on one server calling the apis from the backend of your app hosted on some other server. 

In other terms, CORS is a rule that browser enforces to protect the user's browser from a malicious web page whose JS can read data from some other site the user is logged into. CORS doesn't hold relevant apart from browser context ( a backend making some API calls to third party services using API keys, curl, POSTMAN, Python script).

Use security headers as the first line of defense.

Infrastructure Security --> Preventing app from abuse and ensuring system stays reliable and up during heavy load as well. Use rate limiting ( on a bunch of things, how many password guesses can be made, how many calls of backend api services etc can be made in a given time frame etc).
DDOS protection --> You can use cloud level services like AWS shield or Cloudflare but you need to have application level protection as well. Use graceful degradation, under heavy load, your application should gradually reduce functionality, rather than crash severely. 

Denial of Service (DOS)  is when the haccker makes a bunch of calls manually or programmatically to crash your app. Distributed Denial Of Service ( DDOS ) is when the hacker hacks a bunch of machines and then impersonates them to then make a bunch of programmatic calls from different device to flood your backend with requests and eventually crash it

Security Monitoring --> Set up realtime monitoring alerts, security patches and stuff.

-----------------------------------------------------------
30/8/26 (21:58)

Ensuring your VPS is secured involves -->

1. Disabled root login
2. Created non root sudo user
3. Disabled password authentication
4. Setup UFW
5. Installed Fail2Ban
6. Security update patches frequently and other updates and upgrades.

Always login using SSH keys and that too using the non root user.

When an app hosted on your server listens on 0.0.0.0:3001, it's a wildcard that says, I'll listen to and accept all the connections at any door on port 3001, this could be your 127.0.0.1 ( the loopback address ), your public IPV4 address, or tailscale IP and this is really not a good thing. Since you can't directly access 127.0.0.1 because you are on a server so its technically best to just use tailscale in such cases ( where let's say your phone, local laptop etc are on the tailscale VPN) , use it its kinda secure, bind your app to the tailscale IP of the server. When you are on tailscale VPN, all the devices on that VPN, have unique IPs given by tailscale and that doesn't collide with anything else on the general internet ( because it chooses from CGNAT space of IPs). Also the tailscale IPs in a VPN, can only be accessed by devices in that VPN, any random person typing that would get nothing. 

------------------------------------------------------------

30/8/26 (23:42)

Deploying OkGTM

1. npx convex deploy from the project root where convex is setup. This helps you first deploy the backend to prod from VPS itself and it gives you a prod backend URL that your frontend app will talk to in production.
2. Now you need to set up backend env variables from the VPS command line using npx convex env set ( and use the prod backend for CONVEX_DEPLOYMENT) ( can check finally using the npx convex env list)

At this point, your prod backend stuff is configured, now comes the frontend.

3. Push the app to github, go to vercel, add project and import the repo. It will ask you to set up env keys and it will include the ones that you already set in backend, you can just ignore them and set the NEXT_PUBLIC_CONVEX_URL so that your app talks to the prod backend and deploy, just ignore other suggestions unless relevant.

4. App goes live with vercel subdomain. You can then connect your domain that you already configured in Vercel. Configure if not already configured.

------------------------------------------------------------

--> TODO -->

--> need to properly understand the difference between agent, harness, agent harness , harness engineering, how to spin up sub agents, how to configure that, what does "give your agents access to the cloud" paradigm, what is this graph engineering and stuff.
--> What is scaffolding ?
--> Github Based Deployment vs Docker Based Deployments ?
--> What exactly does open weight models mean ? Why do some models have fewer guard rails for tasks like scraping while others have more ? Is it about the harness or just about the model capabilities ?
--> What does MOE models mean ?
--> Lite LLM seems to be an interesting tool for using CLaude Code harness without any subscription ?
--> Understand how OAuth, JWT, sessions, cookies etc stuff works ?
--> How does HTTP / HTTPS / SSL / TLS certificate works ?
--> What is Cache invalidation ?
--> Understand how TailScale works fundamentally ?
--> How to decide when you need multiple backends ?
--> What is CDN and how does it work ?