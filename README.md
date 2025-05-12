# 🧠 AgenticFlow: Strategic AI Agent Framework

---

## 🔄 Overview

**AgenticFlow** is a strategic AI agent framework capable of executing complex workflows using both symbolic and learned planning techniques.

* A **dynamic agent workflow** enables flexible decision-making.
* Each **context or step** behaves like an object in OOP, with defined **inputs, prompts, tools, and outputs**.
* A **workflow** is structured as a **chain, tree, or graph** of these contexts or steps.
* The **LLM** receives user requests and routes them to the **action model**.
* A **UI interface** allows users to design specific workflow applications via a UI, which are then passed to the action model.
* The **action model** uses the provided request and workflow to determine the optimal response using strategic planning methods—such as **Depth-First Search**, **Breadth-First Search**, **Monte Carlo Tree Search**, or other appropriate algorithms.
* These strategies can be **trained into the model** to improve performance over time.

This enables the development of flexible, extensible, and trainable agent-based applications with robust planning and reasoning capabilities.

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/agenticflow.git
cd agenticflow
```

2. Create a virtual environment (optional but recommended):

```bash
# Using conda
conda create -n agenticflow python=3.10
conda activate agenticflow

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:

```bash
pip install -e .
```

4. Set up your OpenAI API key (if using LLM features):

```bash
export OPENAI_API_KEY=your_api_key_here
```

---

## 🔍 Quick Start

### Running the Sample Workflow

```bash
python main.py
```

This will run the sample workflow using the default Depth-First Search (DFS) strategy.

### Using Different Strategies

```bash
python main.py --strategy bfs  # Breadth-First Search
python main.py --strategy mcts  # Monte Carlo Tree Search
```

### Using the Interactive UI

```bash
python main.py --ui
```

---

## 📚 Framework Architecture

### Core Components

1. **Context**: Represents a step in a workflow with inputs, prompts, tools, and outputs.
2. **Workflow**: Manages contexts as a chain, tree, or graph structure.
3. **ActionModel**: Executes workflows using strategic planning methods.

### Strategies

- **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking.
- **BFS (Breadth-First Search)**: Explores all nodes at the present depth before moving to nodes at the next depth level.
- **MCTS (Monte Carlo Tree Search)**: Uses random sampling to find the optimal path through the workflow.

### Tools System

AgenticFlow includes a tool registry system that allows you to register and use tools within your workflows:

```python
from agenticflow.tools.base import register_tool

@register_tool(
    name="my_custom_tool",
    description="A custom tool for my workflow"
)
def my_custom_tool(param1, param2):
    # Tool implementation
    return result
```

---

## 🛠️ Creating Custom Workflows

Here's a simple example of creating a custom workflow:

```python
from agenticflow.core.workflow import Workflow
from agenticflow.core.context import Context
from agenticflow.core.action_model import ActionModel

# Create a workflow
workflow = Workflow(
    name="My Custom Workflow",
    description="A simple custom workflow"
)

# Create contexts
context1 = Context(
    id="step1",
    name="First Step",
    description="The first step in the workflow",
    prompt_template="Process this input: {input}"
)

context2 = Context(
    id="step2",
    name="Second Step",
    description="The second step in the workflow",
    prompt_template="Continue processing: {step1_output}"
)

# Define run functions
def run_step1(context):
    input_value = context.inputs.get("input", "")
    # Process the input
    return {"step1_output": f"Processed: {input_value}"}

def run_step2(context):
    step1_output = context.inputs.get("step1_output", "")
    # Process further
    return {"final_output": f"Final result: {step1_output}"}

# Set run functions
context1.set_run_function(run_step1)
context2.set_run_function(run_step2)

# Add contexts to workflow
workflow.add_context(context1)
workflow.add_context(context2)

# Connect contexts
workflow.connect("step1", "step2")

# Execute the workflow
action_model = ActionModel()
result = action_model.execute(
    workflow=workflow,
    strategy="dfs",
    initial_data={"input": "Hello, AgenticFlow!"}
)

print(result["final_output"])
```

For more complex examples, check the `examples/` directory.

---

## 📊 Visualizing Workflows

AgenticFlow provides built-in visualization capabilities using NetworkX and Matplotlib:

```python
workflow.visualize("my_workflow.png")
```

This will generate a visual representation of your workflow, showing all contexts and their connections.

---

## 🔁 Comparison: AgenticFlow vs. Existing Frameworks

| Feature / Concept                                        | Overlap With                       | Description                                                   |
| -------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **Dynamic agent workflows as graphs**                    | LangGraph, AutoGen, CrewAI         | Similar in enabling DAG-based agent behavior.                 |
| **Context/Step as OOP-like unit (input, tools, output)** | LangChain Runnable, LangGraph Node | Aligns with LangChain’s modular `Runnable` abstraction.       |
| **Workflow built via UI and executed by model**          | MetaGPT, SuperAGI, Smol-dev        | Indirect overlap; UI-based orchestration is rare.             |
| **Strategy-based traversal (DFS, MCTS, etc.)**           | Agent-Q                            |                                                               |
| **Training strategy models**                             | Unity ML-Agents (in robotics)      | LLM frameworks don’t typically include trainable planners.    |

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

- **AgentQ**
  [https://github.com/sentient-engineering/agent-q](https://github.com/sentient-engineering/agent-q)

- **LangFlow**
  [https://github.com/langflow-ai/langflow](https://github.com/langflow-ai/langflow)
