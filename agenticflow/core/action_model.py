"""Action Model module for AgenticFlow framework.

This module defines the ActionModel class which is responsible for executing workflows
using strategic planning methods.
"""

from typing import Dict, List, Any, Optional, Callable
from .workflow import Workflow
from .context import Context


class ActionModel:
    """Action Model for executing workflows using strategic planning.
    
    The action model uses the provided request and workflow to determine
    the optimal response using strategic planning methods.
    """
    
    def __init__(self):
        """Initialize the action model."""
        self.strategies = {}
        
    def register_strategy(self, name: str, strategy_func: Callable) -> None:
        """Register a strategy for workflow execution."""
        self.strategies[name] = strategy_func
        
    def execute(self, workflow: Workflow, strategy: str = "dfs", initial_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a workflow using the specified strategy."""
        if strategy not in self.strategies:
            raise ValueError(f"Strategy '{strategy}' not registered")
        
        # Initialize data
        data = initial_data or {}
        
        # Execute the workflow using the selected strategy
        return self.strategies[strategy](workflow, data)
    
    def execute_context(self, context: Context, data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single context with the given data."""
        # Prepare inputs for the context
        inputs = {k: data.get(k) for k in context.inputs.keys() if k in data}
        
        # Execute the context
        result = context.run(**inputs)
        
        # Update the data with the context outputs
        data.update(result)
        
        return data
