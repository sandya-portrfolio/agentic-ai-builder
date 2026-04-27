# AI-DevOpsAgent_Claude
Take a project idea - Generate code -  Create folder structure - Zip it Push to GitHub

**Architecture **
Agents:
Planner Agent
→ breaks project into steps
Code Generator Agent
→ writes files
File Builder Agent
→ creates folder + files
Packager Agent
→ creates ZIP
GitHub Agent
→ pushes repo
Step-by-step implementation (Windows)
1️⃣ Install required tools
pip install openai anthropic langchain crewai python-dotenv GitPython

2️⃣ Project structure
agentic-ai-builder/
│
├── agents/
│   ├── planner.py
│   ├── coder.py
│   ├── packager.py
│   ├── github_agent.py
│
├── output/
├── main.py
├── .env

3️⃣ Example: Simple Agentic Builder
