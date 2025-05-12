"""Context module for AgenticFlow framework.

This module defines the Context class which represents a step in a workflow.
Each context has inputs, prompts, tools, and outputs, similar to an object in OOP.
"""

from typing import Dict, List, Any, Callable, Optional
from pydantic import BaseModel, Field


class Context(BaseModel):
    """A context or step in a workflow.
    
    Each context behaves like an object in OOP, with defined inputs, prompts, tools, and outputs.
    """
    
    id: str
    name: str
    description: str = ""
    inputs: Dict[str, Any] = Field(default_factory=dict)
    outputs: Dict[str, Any] = Field(default_factory=dict)
    tools: List[Any] = Field(default_factory=list)
    prompt_template: str = ""
    
    # Function to execute when this context is run
    _run_func: Optional[Callable] = None
    
    def set_run_function(self, func: Callable) -> None:
        """Set the function to run when this context is executed."""
        self._run_func = func
    
    def run(self, **kwargs) -> Dict[str, Any]:
        """Run this context with the given inputs."""
        if self._run_func is None:
            raise ValueError(f"No run function set for context {self.id}")
        
        # Update inputs with kwargs
        for key, value in kwargs.items():
            self.inputs[key] = value
            
        # Run the function
        result = self._run_func(self)
        
        # Update outputs
        if isinstance(result, dict):
            self.outputs.update(result)
        
        return self.outputs
    
    def __str__(self) -> str:
        return f"Context({self.id}: {self.name})"
    
    def __repr__(self) -> str:
        return self.__str__()
