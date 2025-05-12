"""Example of creating and running a custom workflow with AgenticFlow."""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agenticflow.core.workflow import Workflow
from agenticflow.core.context import Context
from agenticflow.core.action_model import ActionModel
from agenticflow.strategies.registry import default_registry


def create_custom_workflow() -> Workflow:
    """Create a custom workflow for text analysis."""
    # Create a new workflow
    workflow = Workflow(
        name="Text Analysis Workflow",
        description="A workflow that analyzes text and provides insights"
    )
    
    # Create contexts
    text_input_context = Context(
        id="text_input",
        name="Text Input",
        description="Get text input for analysis",
        prompt_template="Please provide text for analysis: {text_input}"
    )
    
    sentiment_analysis_context = Context(
        id="sentiment_analysis",
        name="Sentiment Analysis",
        description="Analyze the sentiment of the text",
        prompt_template="Analyze the sentiment of the following text: {text_input}"
    )
    
    entity_extraction_context = Context(
        id="entity_extraction",
        name="Entity Extraction",
        description="Extract entities from the text",
        prompt_template="Extract entities from the following text: {text_input}"
    )
    
    summary_context = Context(
        id="summary",
        name="Text Summary",
        description="Generate a summary of the text",
        prompt_template="Generate a summary of the following text: {text_input}"
    )
    
    insights_context = Context(
        id="insights",
        name="Generate Insights",
        description="Generate insights based on all analyses",
        prompt_template="Generate insights based on the following analyses:\n\nText: {text_input}\nSentiment: {sentiment}\nEntities: {entities}\nSummary: {summary}"
    )
    
    # Define run functions for each context
    def run_text_input(context):
        # For this example, we'll use a hardcoded text input
        # In a real application, this could come from user input or a file
        text = """
        AgenticFlow is a strategic AI agent framework capable of executing complex workflows 
        using both symbolic and learned planning techniques. It enables the development of 
        flexible, extensible, and trainable agent-based applications with robust planning 
        and reasoning capabilities.
        """
        return {"text_input": text}
    
    def run_sentiment_analysis(context):
        text = context.inputs.get("text_input", "")
        # In a real application, this would use an NLP model or API
        sentiment = "Positive - The text describes a framework with positive attributes like 'flexible', 'extensible', and 'robust'"
        return {"sentiment": sentiment}
    
    def run_entity_extraction(context):
        text = context.inputs.get("text_input", "")
        # In a real application, this would use an NLP model or API
        entities = [
            {"type": "FRAMEWORK", "text": "AgenticFlow"},
            {"type": "CONCEPT", "text": "strategic AI agent framework"},
            {"type": "CAPABILITY", "text": "symbolic and learned planning techniques"},
            {"type": "ATTRIBUTE", "text": "flexible"},
            {"type": "ATTRIBUTE", "text": "extensible"},
            {"type": "ATTRIBUTE", "text": "trainable"},
        ]
        return {"entities": entities}
    
    def run_summary(context):
        text = context.inputs.get("text_input", "")
        # In a real application, this would use an NLP model or API
        summary = "AgenticFlow is an AI framework for creating flexible and trainable agent-based applications with advanced planning capabilities."
        return {"summary": summary}
    
    def run_insights(context):
        text = context.inputs.get("text_input", "")
        sentiment = context.inputs.get("sentiment", "")
        entities = context.inputs.get("entities", [])
        summary = context.inputs.get("summary", "")
        
        # Generate insights based on all analyses
        insights = """
        Key Insights:
        1. AgenticFlow positions itself as a strategic framework, emphasizing planning capabilities
        2. The framework focuses on flexibility and extensibility, suggesting it's designed for diverse applications
        3. The mention of "trainable" indicates machine learning capabilities
        4. The framework appears to combine symbolic AI with machine learning approaches
        
        Potential Applications:
        - Complex decision-making systems requiring strategic planning
        - Workflow automation with adaptive learning capabilities
        - Multi-agent systems with sophisticated coordination requirements
        """
        
        return {"insights": insights}
    
    # Set run functions for each context
    text_input_context.set_run_function(run_text_input)
    sentiment_analysis_context.set_run_function(run_sentiment_analysis)
    entity_extraction_context.set_run_function(run_entity_extraction)
    summary_context.set_run_function(run_summary)
    insights_context.set_run_function(run_insights)
    
    # Add contexts to workflow
    workflow.add_context(text_input_context)
    workflow.add_context(sentiment_analysis_context)
    workflow.add_context(entity_extraction_context)
    workflow.add_context(summary_context)
    workflow.add_context(insights_context)
    
    # Connect contexts - this creates a more complex graph structure
    workflow.connect("text_input", "sentiment_analysis")
    workflow.connect("text_input", "entity_extraction")
    workflow.connect("text_input", "summary")
    workflow.connect("sentiment_analysis", "insights")
    workflow.connect("entity_extraction", "insights")
    workflow.connect("summary", "insights")
    
    return workflow


def run_workflow(strategy="dfs"):
    """Run the custom workflow with the specified strategy."""
    print(f"Running custom workflow with {strategy} strategy...\n")
    
    # Create the workflow
    workflow = create_custom_workflow()
    
    # Create an action model
    action_model = ActionModel()
    
    # Register strategies
    for name, strategy_func in default_registry.strategies.items():
        action_model.register_strategy(name, strategy_func)
    
    # Execute the workflow
    result = action_model.execute(workflow, strategy=strategy)
    
    # Print the result
    print("\nWorkflow execution complete!\n")
    print("Text Analysis Results:")
    print("-" * 40)
    print(f"Sentiment: {result.get('sentiment', 'N/A')}")
    print("\nEntities:")
    for entity in result.get('entities', []):
        print(f"  - {entity['type']}: {entity['text']}")
    print(f"\nSummary: {result.get('summary', 'N/A')}")
    print("\nInsights:")
    print(result.get('insights', 'No insights generated'))
    
    return result


if __name__ == "__main__":
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    
    # Default to DFS, but you can change this to 'bfs' or 'mcts'
    run_workflow("dfs")
    
    # Visualize the workflow (requires matplotlib)
    try:
        import matplotlib.pyplot as plt
        workflow = create_custom_workflow()
        workflow.visualize("text_analysis_workflow.png")
        print("\nWorkflow visualization saved to text_analysis_workflow.png")
    except ImportError:
        print("\nMatplotlib is required for visualization")
