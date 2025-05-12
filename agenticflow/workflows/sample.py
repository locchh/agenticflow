"""Sample workflow for AgenticFlow framework."""

from ..core.workflow import Workflow
from ..core.context import Context
from ..tools.base import get_tool


def create_sample_workflow() -> Workflow:
    """Create a sample workflow for demonstration purposes."""
    # Create a new workflow
    workflow = Workflow(
        name="Sample Workflow",
        description="A sample workflow demonstrating AgenticFlow capabilities"
    )
    
    # Create contexts
    input_context = Context(
        id="input",
        name="User Input",
        description="Collect input from the user",
        prompt_template="Please provide your question or request: {user_input}"
    )
    
    process_context = Context(
        id="process",
        name="Process Input",
        description="Process the user input",
        prompt_template="Process the following user input: {user_input}"
    )
    
    search_context = Context(
        id="search",
        name="Search Information",
        description="Search for information related to the user input",
        prompt_template="Search for information about: {processed_input}"
    )
    
    generate_context = Context(
        id="generate",
        name="Generate Response",
        description="Generate a response based on the search results",
        prompt_template="Generate a response based on the following information:\n\nUser input: {user_input}\nProcessed input: {processed_input}\nSearch results: {search_results}"
    )
    
    output_context = Context(
        id="output",
        name="Format Output",
        description="Format the response for the user",
        prompt_template="Format the following response for the user:\n\n{generated_response}"
    )
    
    # Define run functions for each context
    def run_input(context):
        # In a real application, this would collect input from the user
        return {"user_input": "How does AgenticFlow compare to LangChain?"}
    
    def run_process(context):
        # Process the user input
        user_input = context.inputs.get("user_input", "")
        # In a real application, this would use an LLM to process the input
        processed_input = f"Comparison between AgenticFlow and LangChain frameworks"
        return {"processed_input": processed_input}
    
    def run_search(context):
        # Search for information
        processed_input = context.inputs.get("processed_input", "")
        # In a real application, this would use a search tool
        search_results = """
        AgenticFlow is a strategic AI agent framework that focuses on workflow execution using symbolic and learned planning techniques.
        LangChain is a framework for developing applications powered by language models, focusing on composability and integration.
        
        Key differences:
        1. AgenticFlow emphasizes strategic planning and decision-making
        2. LangChain focuses on chaining together different components for LLM applications
        3. AgenticFlow includes trainable strategy models
        4. LangChain has a larger ecosystem of integrations
        """
        return {"search_results": search_results}
    
    def run_generate(context):
        # Generate a response
        user_input = context.inputs.get("user_input", "")
        processed_input = context.inputs.get("processed_input", "")
        search_results = context.inputs.get("search_results", "")
        
        # In a real application, this would use an LLM to generate the response
        generated_response = f"""
        Based on your question about how AgenticFlow compares to LangChain:
        
        AgenticFlow is a strategic AI agent framework that focuses on workflow execution with an emphasis on planning techniques like DFS, BFS, and MCTS. It treats each step as an OOP-like object with defined inputs, prompts, tools, and outputs.
        
        LangChain, on the other hand, is a more general framework for LLM applications with a focus on composability and integrations.
        
        The key advantage of AgenticFlow is its emphasis on strategic planning and trainable strategy models, while LangChain offers a broader ecosystem of integrations and tools.
        """
        
        return {"generated_response": generated_response}
    
    def run_output(context):
        # Format the output
        generated_response = context.inputs.get("generated_response", "")
        
        # In a real application, this might format the response in a specific way
        formatted_response = generated_response.strip()
        
        return {"formatted_response": formatted_response}
    
    # Set run functions for each context
    input_context.set_run_function(run_input)
    process_context.set_run_function(run_process)
    search_context.set_run_function(run_search)
    generate_context.set_run_function(run_generate)
    output_context.set_run_function(run_output)
    
    # Add contexts to workflow
    workflow.add_context(input_context)
    workflow.add_context(process_context)
    workflow.add_context(search_context)
    workflow.add_context(generate_context)
    workflow.add_context(output_context)
    
    # Connect contexts
    workflow.connect("input", "process")
    workflow.connect("process", "search")
    workflow.connect("search", "generate")
    workflow.connect("generate", "output")
    
    return workflow
