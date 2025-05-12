"""Simple UI implementation for AgenticFlow framework."""

from typing import Dict, Any, List, Optional
from ..core.workflow import Workflow
from ..core.context import Context


class SimpleUI:
    """Simple UI for AgenticFlow framework.
    
    This class provides a simple command-line interface for interacting with
    AgenticFlow workflows.
    """
    
    def __init__(self):
        """Initialize the simple UI."""
        self.workflows: Dict[str, Workflow] = {}
    
    def register_workflow(self, workflow: Workflow) -> None:
        """Register a workflow with the UI."""
        self.workflows[workflow.name] = workflow
        
    def list_workflows(self) -> List[str]:
        """List all registered workflows."""
        return list(self.workflows.keys())
    
    def display_workflow(self, workflow_name: str) -> None:
        """Display information about a workflow."""
        if workflow_name not in self.workflows:
            print(f"Workflow '{workflow_name}' not found")
            return
        
        workflow = self.workflows[workflow_name]
        print(f"Workflow: {workflow.name}")
        print(f"Description: {workflow.description}")
        print(f"Contexts: {len(workflow.contexts)}")
        
        # Display contexts
        print("\nContexts:")
        for context_id, context in workflow.contexts.items():
            print(f"  - {context.id}: {context.name}")
            
        # Display connections
        print("\nConnections:")
        for from_id, to_id in workflow.graph.edges():
            from_name = workflow.contexts[from_id].name
            to_name = workflow.contexts[to_id].name
            condition = workflow.graph[from_id][to_id].get('condition', '')
            if condition:
                print(f"  - {from_name} -> {to_name} [if {condition}]")
            else:
                print(f"  - {from_name} -> {to_name}")
    
    def visualize_workflow(self, workflow_name: str, filename: Optional[str] = None) -> None:
        """Visualize a workflow."""
        if workflow_name not in self.workflows:
            print(f"Workflow '{workflow_name}' not found")
            return
        
        workflow = self.workflows[workflow_name]
        workflow.visualize(filename)
        
        if filename:
            print(f"Workflow visualization saved to {filename}")
    
    def run_interactive(self) -> None:
        """Run the UI in interactive mode."""
        print("AgenticFlow Simple UI")
        print("=====================")
        
        while True:
            print("\nAvailable commands:")
            print("  1. List workflows")
            print("  2. Display workflow")
            print("  3. Visualize workflow")
            print("  4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                workflows = self.list_workflows()
                if workflows:
                    print("\nAvailable workflows:")
                    for i, name in enumerate(workflows, 1):
                        print(f"  {i}. {name}")
                else:
                    print("\nNo workflows registered")
                    
            elif choice == "2":
                workflows = self.list_workflows()
                if not workflows:
                    print("\nNo workflows registered")
                    continue
                    
                print("\nAvailable workflows:")
                for i, name in enumerate(workflows, 1):
                    print(f"  {i}. {name}")
                    
                try:
                    idx = int(input("\nEnter workflow number: ")) - 1
                    if 0 <= idx < len(workflows):
                        self.display_workflow(workflows[idx])
                    else:
                        print("Invalid workflow number")
                except ValueError:
                    print("Invalid input")
                    
            elif choice == "3":
                workflows = self.list_workflows()
                if not workflows:
                    print("\nNo workflows registered")
                    continue
                    
                print("\nAvailable workflows:")
                for i, name in enumerate(workflows, 1):
                    print(f"  {i}. {name}")
                    
                try:
                    idx = int(input("\nEnter workflow number: ")) - 1
                    if 0 <= idx < len(workflows):
                        filename = input("Enter filename to save visualization (leave empty to display): ")
                        self.visualize_workflow(workflows[idx], filename or None)
                    else:
                        print("Invalid workflow number")
                except ValueError:
                    print("Invalid input")
                    
            elif choice == "4":
                print("\nExiting AgenticFlow UI")
                break
                
            else:
                print("\nInvalid choice. Please enter a number between 1 and 4.")
