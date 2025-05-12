"""Main script to demonstrate the AgenticFlow framework."""

import os
import argparse
from agenticflow.core.action_model import ActionModel
from agenticflow.strategies.registry import default_registry
from agenticflow.workflows.sample import create_sample_workflow
from agenticflow.ui.simple_ui import SimpleUI


def run_sample_workflow(strategy="dfs"):
    """Run the sample workflow with the specified strategy."""
    print(f"Running sample workflow with {strategy} strategy...")
    
    # Create the sample workflow
    workflow = create_sample_workflow()
    
    # Create an action model
    action_model = ActionModel()
    
    # Register strategies
    for name, strategy_func in default_registry.strategies.items():
        action_model.register_strategy(name, strategy_func)
    
    # Execute the workflow
    result = action_model.execute(workflow, strategy=strategy)
    
    # Print the result
    print("\nWorkflow execution complete!")
    print("\nResult:")
    for key, value in result.items():
        if key == "formatted_response":
            print(f"\n{value}")
    
    return result


def run_interactive_ui():
    """Run the interactive UI."""
    ui = SimpleUI()
    
    # Register the sample workflow
    workflow = create_sample_workflow()
    ui.register_workflow(workflow)
    
    # Run the UI
    ui.run_interactive()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="AgenticFlow Demo")
    parser.add_argument("--ui", action="store_true", help="Run the interactive UI")
    parser.add_argument("--strategy", type=str, default="dfs", choices=["dfs", "bfs", "mcts"],
                       help="Strategy to use for workflow execution")
    args = parser.parse_args()
    
    if args.ui:
        run_interactive_ui()
    else:
        run_sample_workflow(args.strategy)


if __name__ == "__main__":
    main()
