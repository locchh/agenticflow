"""Base tool implementation for AgenticFlow framework."""

from typing import Dict, Any, Callable, Optional, List
from pydantic import BaseModel, Field


class Tool(BaseModel):
    """Base class for tools in AgenticFlow.
    
    Tools provide functionality that can be used by contexts in a workflow.
    """
    
    name: str
    description: str
    func: Callable
    
    def run(self, **kwargs) -> Any:
        """Run the tool with the given arguments."""
        return self.func(**kwargs)
    
    def __call__(self, **kwargs) -> Any:
        """Allow the tool to be called directly."""
        return self.run(**kwargs)


class ToolRegistry:
    """Registry for tools in AgenticFlow."""
    
    def __init__(self):
        """Initialize an empty tool registry."""
        self.tools: Dict[str, Tool] = {}
    
    def register(self, tool: Tool) -> None:
        """Register a tool in the registry."""
        if tool.name in self.tools:
            raise ValueError(f"Tool with name '{tool.name}' already registered")
        self.tools[tool.name] = tool
    
    def get(self, name: str) -> Tool:
        """Get a tool by name."""
        if name not in self.tools:
            raise ValueError(f"Tool with name '{name}' not found in registry")
        return self.tools[name]
    
    def list_tools(self) -> List[Tool]:
        """List all registered tools."""
        return list(self.tools.values())


# Create a global instance of the tool registry
default_registry = ToolRegistry()


def register_tool(name: str, description: str, func: Callable) -> Tool:
    """Register a tool in the default registry."""
    tool = Tool(name=name, description=description, func=func)
    default_registry.register(tool)
    return tool


def get_tool(name: str) -> Tool:
    """Get a tool from the default registry."""
    return default_registry.get(name)
