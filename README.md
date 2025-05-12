# 🧠 AgenticFlow: Strategic AI Agent Framework

---

## 🔄 Overview

**AgenticFlow** is a strategic AI agent framework capable of executing complex workflows using both symbolic and learned planning techniques.

* A **dynamic agent workflow** enables flexible decision-making.
* Each **context or step** behaves like an object in OOP, with defined **inputs, prompts, tools, and outputs**.
* A **workflow** is structured as a **chain, tree, or graph** of these contexts or steps.
* The **LLM** receives user requests and routes them to the **action model**.
* A **builder interface** allows users to design specific workflow applications via a UI, which are then passed to the action model.
* The **action model** uses the provided request and workflow to determine the optimal response using strategic planning methods—such as **Depth-First Search**, **Breadth-First Search**, **Monte Carlo Tree Search**, or other appropriate algorithms.
* These strategies can be **trained into the model** to improve performance over time.

### Key Features

- A modular, graph-based execution engine.
- An intelligent **action model** that selects the best traversal strategy (e.g., DFS, BFS, MCTS).
- A **Builder UI** for visually constructing agent workflows.
- Support for **training models** to dynamically select or blend traversal strategies based on context.

This enables the development of flexible, extensible, and trainable agent-based applications with robust planning and reasoning capabilities.

---

## 🔁 Comparison: AgenticFlow vs. Existing Frameworks

| Feature / Concept                                        | Overlap With                       | Description                                                   |
| -------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **Dynamic agent workflows as graphs**                    | LangGraph, AutoGen, CrewAI         | Similar in enabling DAG-based agent behavior.                 |
| **Context/Step as OOP-like unit (input, tools, output)** | LangChain Runnable, LangGraph Node | Aligns with LangChain’s modular `Runnable` abstraction.       |
| **Workflow built via UI and executed by model**          | MetaGPT, SuperAGI, Smol-dev        | Indirect overlap; UI-based orchestration is rare.             |
| **Strategy-based traversal (DFS, MCTS, etc.)**           | None                               | Original idea; not found in other agent frameworks.           |
| **Training strategy models**                             | Unity ML-Agents (in robotics)      | LLM frameworks don’t typically include trainable planners.    |

---

## 🧠 What Makes AgenticFlow Unique

1. **Graph Traversal as a Reasoning Strategy**  
   Workflows are searched using symbolic algorithms (DFS, BFS, MCTS), enabling adaptive and optimal decision-making.

2. **Trainable Planner / Strategy Selector**  
   The system can learn which traversal strategy fits a given workflow, blending classical search with ML or RL policy optimization.

3. **Visual Builder to Runtime Execution Flow**  
   A full-stack connection from a visual workflow designer to an action model that interprets and executes plans dynamically.

4. **Modular Step Architecture**  
   Each step is encapsulated like a class with inputs, prompts, tools, and outputs — making the system reusable and composable.

---

## 🔗 Related Frameworks

| Framework               | Role                      | Notes                                                           |
| ----------------------- | ------------------------- | ---------------------------------------------------------------- |
| **LangGraph**           | Workflow Graph Execution  | Ideal for building the DAG-based agent system.                  |
| **LangChain**           | Tool & Prompt Abstraction | Provides reusable components for prompts, tools, and memory.    |
| **AutoGen**             | Multi-Agent Communication | Useful for coordinating agents in conversation-based workflows. |
| **CrewAI**              | Team-based Agents         | Good model for role-based task delegation.                      |
| **MetaGPT**             | Developer Agents          | Simulates multiple agent roles; can inspire structure.          |
| **Smol-dev/SmolAgents** | Coding Agents             | Lightweight, good inspiration for step abstraction.             |
| **Unity ML-Agents**     | Trainable Agent Behaviors | Inspiration for learning-based strategy execution (non-LLM).    |
| **NetworkX**            | Graph Algorithms          | Excellent for implementing traversal algorithms like DFS, MCTS. |
| **AgentFlow**           | Agent Execution Flow      | A modular system for defining and executing LLM agent steps.    |

---

## 📚 References

- **LangChain**  
  [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)  
  Modular framework for developing LLM-powered applications using tools, memory, and chains.

- **LangGraph**  
  [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)  
  State-machine extension of LangChain that allows for building complex agent workflows with graph structures.

- **AutoGen**  
  [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)  
  Microsoft’s framework for building LLM-powered multi-agent systems with communication protocols.

- **CrewAI**  
  [https://github.com/joaomdmoura/crewai](https://github.com/joaomdmoura/crewai)  
  Agent framework inspired by human-like team structures and delegation.

- **MetaGPT**  
  [https://github.com/geekan/MetaGPT](https://github.com/geekan/MetaGPT)  
  Multi-agent framework that mimics the software engineering team workflow using GPT agents.

- **Smol-dev / SmolAgents**  
  [https://github.com/smol-ai/agents](https://github.com/smol-ai/agents)  
  Minimal, autonomous agents for task automation and project generation.

- **Unity ML-Agents**  
  [https://github.com/Unity-Technologies/ml-agents](https://github.com/Unity-Technologies/ml-agents)  
  Toolkit for training intelligent agents using reinforcement learning inside Unity environments.

- **NetworkX**  
  [https://networkx.org/](https://networkx.org/)  
  Python library for creating and manipulating complex graphs and implementing algorithms like DFS, BFS, and MCTS.

- **AgentFlow**  
  [https://github.com/simonmesmith/agentflow](https://github.com/simonmesmith/agentflow)  
  A lightweight framework for composing and executing LLM agent pipelines using modular, composable components.
