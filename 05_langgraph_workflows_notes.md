# 📘 Agentic AI with LangGraph

## 🧠 **In-Depth Notes: Core Concepts & Practical Workflows**

---

### 📺 **Introduction & Playlist Recap**

- **Instructor**: Nitesh (Agentic AI using LangGraph playlist)
- **Previous Sessions**:
  - **Conceptual foundations**: Generative AI vs Agentic AI
  - **LangChain vs LangGraph**: Why shift from chains to graphs?
  - **LangGraph Theory**: Nodes, edges, state, and graph compilation.
- **Current Focus**: Moving from theory to **practical coding demonstrations**.
- **Goal**: Equip learners to independently build **sequential and complex workflows**.

---

### 🗂️ **LangGraph: Orchestrating LLM Workflows**

- **LangGraph Overview**:
  - A Python library for modeling AI workflows as **graphs**.
  - **Nodes** = Units of work (LLM calls, functions, tools).
  - **Edges** = Flow of control and data.

- **Why LangGraph?**
  - Enables **stateful, resumable, and parallel workflows**.
  - Integrates cleanly with **LangChain** components (models, prompts, loaders).

- **Key Features**:
  - ✅ Visual workflow representation
  - ✅ Parallelism & branching
  - ✅ Built-in memory management
  - ✅ Resumability for long-running tasks

---

### 🔁 **Core Workflow Patterns**

#### 1️⃣ Sequential Workflow
- **Flow**: Task A → Task B → Task C.
- **Example**: Calculate BMI → Classify fitness category.
- **Use Case**: Simple linear processes.

#### 2️⃣ Prompt Chaining
- **Flow**: Topic → Generate Outline → Draft Blog → Evaluate.
- **Example**: Build a blog with multiple LLM calls.

#### 3️⃣ Parallel Execution
- **Flow**: Task A1, A2, A3 run simultaneously.
- **Example**: Moderating content for multiple policies at once.

#### 4️⃣ Conditional Routing
- **Flow**: Based on state, choose Task B or Task C.
- **Example**: Route user query to refund handler or sales agent.

---

### 🧱 **Key Concepts: Nodes, Edges, State**

- **Nodes**: Python functions performing tasks. E.g., calculate_bmi(), generate_outline().
- **Edges**: Define the connections between nodes (linear, conditional, loops).
- **State**: Shared mutable data passed across nodes.
  - **Example**: `{ weight: float, height: float, bmi: float }`
  - Encapsulated using **TypedDict** for type safety.

---

### ⚙️ **Step-by-Step: From Setup to Execution**

#### 🖥️ Environment Setup
1. Create project folder: `LangGraph_Tutorials`
2. Initialize virtual environment: `python -m venv myenv`
3. Install libraries: `pip install langgraph langchain openai ipykernel`
4. Launch Jupyter Notebook for visual experimentation.

#### 📝 Workflow Example: BMI Calculator
- **State**: `{ weight, height, bmi }`
- **Graph Flow**:
  - Start → calculate_bmi → end
- **Node Logic**:
  - `calculate_bmi(state)`: Computes BMI and updates state.
- **Execution**: Run workflow with input state, receive final output with BMI.

#### 📝 Enhanced Workflow: BMI Categorizer
- Add new node `label_bmi()` after BMI calculation.
- Update state to include `category: str`
- Workflow Flow: Start → calculate_bmi → label_bmi → end.

#### 🤖 Simple LLM Workflow
- Input question → Query OpenAI LLM → Store answer in state.
- Demonstrates integration with LangChain models.

#### 📝 Prompt Chaining Workflow
- Title → Generate Outline → Create Blog.
- Shows multi-step LLM interactions and state propagation.

---

### 🚀 **Execution Model**

1. **Define Graph**:
   - Nodes, edges, and state schema.
2. **Compile Graph**:
   - Validates structure and prepares execution.
3. **Execute Workflow**:
   - Feed initial state → Nodes process sequentially or in parallel → Final state produced.

**Key Mechanisms**:
- **Reducers**: Merge partial updates from parallel nodes.
- **Supersteps**: Handle groups of simultaneous node executions.
- **Visualization**: View workflow graphs directly in Jupyter Notebook.

---

### ✅ **Key Takeaways**

- **LangGraph** enables complex LLM workflows with minimal boilerplate.
- Builds on **LangChain** components while adding orchestration and state management.
- Supports both **simple sequential workflows** and **advanced agentic architectures**.
- Essential for production-grade AI systems requiring **resilience, parallelism, and memory**.

---

### 📚 **Further Reading & Resources**
- [LangGraph Documentation](https://docs.langgraph.org)
- [LangChain Documentation](https://docs.langchain.com)
- Research Papers on Agentic AI: *TBD*

---

