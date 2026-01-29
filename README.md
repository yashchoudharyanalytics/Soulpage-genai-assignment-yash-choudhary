# 1. Clone the repository
git clone https://github.com/yashchoudharyanalytics/Soulpage-genai-assignment-yash-choudhary.git 
cd Soulpage-genai-assignment-yash-choudhary

# 2. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Set OpenAI API Key
set OPENAI_API_KEY=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   # Windows

# 5. Launch the Streamlit UI
streamlit run app.py































Soulpage GenAI Assignment
Unified Agentic AI System: Conversational Intelligence → Multi-Agent Reasoning

Executive Summary (Read This First)

This project deliberately avoids considering Task 1 and Task 2 as separate issues.

Rather, it offers a single, integrated Agentic AI solution, in which:

Task 2 (Conversational Knowledge Bot) serves as the basis

Task 1 (Multi-Agent System) is a natural extension thereof

Why I Did NOT Implement the Tasks Separately
Task 1 → a standalone multi-agent script
Task 2 → a separate chatbot

No shared memory, no architectural continuity

This leads to:
Code duplication
Fragmented logic
No explanation of how systems evolve in real products

My Design Decision 
I treated Task 2 as the base layer and Task 1 as an advanced layer, because:
A multi-agent system is meaningless without a strong single-agent foundation.

Architectural reasoning:
Task 2 already demonstrates:
LLM reasoning
Tool usage
Memory
Context handling
Task 1 simply specializes and scales this capability across multiple agents with distinct roles


Single-Agent (Task 2)
│
├── LLM reasoning
├── Memory
├── Tool usage
│
▼
Multi-Agent Extension (Task 1)
│
├── Agent 1: Data Collection (tools only)
├── Agent 2: Analysis & Reasoning
└── Orchestrator: Controls execution flow

Task 2: Conversational Knowledge Base (Foundation Layer)
Conversational agent capable of:
Remembering past interactions
Fetching external knowledge when needed
Responding contextually

Key Components
LLM: ChatOpenAI
Memory: ConversationBufferMemory
Tool: DuckDuckGo Web Search
Agent Type: Function-calling agent
Interface: Streamlit Chat UI

This layer proves:
I understand why LLMs hallucinate
How tools reduce hallucinations
Why memory must be explicit
How agents decide when to use tools

Task 1: Multi-Agent Market Intelligence System (Advanced Layer)

Agents Implemented
1️. Data Collector Agent
Role: Fetch raw company data
Tools: Web search
Constraint:  No analysis,  no summarization

2️. Analyst Agent
Role: Analyze provided data
Output: Insights, summaries, risks
Constraint: Uses only collector output

3️. Orchestrator
Controls execution order
Passes data between agents
Produces final response

This shows:
Agent role clarity
Deterministic orchestration

Both tasks are exposed through one clean UI, because in real products:
Users don’t care how many agents exist; they care about outcomes.

UI Features:
Sidebar navigation
Conversational chat interface
Multi-agent execution trigger
Graceful handling of API limitations

Due to OpenAI API quota limitations:
Live responses may not always execute
However:
All agents initialize correctly
Tool + memory wiring is complete
Orchestration flow is correct
Failures are handled gracefully in UI

PROJECT STRUCTURE

Soulpage-genai-assignment-yash-choudhary/
│
├── app.py                         # Unified Streamlit UI
├── core/
│   ├── llm.py                     # LLM initialization
│   ├── memory.py                  # Conversation memory
│   └── tools.py                   # External tools
│
├── task2_conversational_bot/
│   └── chat_agent.py              # Base conversational agent
│
├── task1_multi_agent/
│   ├── data_collector_agent.py
│   ├── analyst_agent.py
│   └── orchestrator.py
│
├── requirements.txt
└── README.md
