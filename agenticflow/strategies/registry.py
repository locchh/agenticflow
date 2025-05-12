"""Strategy registry for AgenticFlow framework."""

from typing import Dict, Callable, Any
from ..core.workflow import Workflow
from .dfs import dfs_strategy
from .bfs import bfs_strategy
from .mcts import mcts_strategy


class StrategyRegistry:
    """Registry for workflow execution strategies."""
    
    def __init__(self):
        """Initialize the strategy registry with default strategies."""
        self.strategies = {
            "dfs": dfs_strategy,
            "bfs": bfs_strategy,
            "mcts": mcts_strategy,
        }
    
    def register(self, name: str, strategy_func: Callable) -> None:
        """Register a new strategy."""
        self.strategies[name] = strategy_func
    
    def get(self, name: str) -> Callable:
        """Get a strategy by name."""
        if name not in self.strategies:
            raise ValueError(f"Strategy '{name}' not found in registry")
        return self.strategies[name]
    
    def list_strategies(self) -> Dict[str, Callable]:
        """List all registered strategies."""
        return self.strategies


# Create a global instance of the strategy registry
default_registry = StrategyRegistry()


def register_strategy(name: str, strategy_func: Callable) -> None:
    """Register a strategy in the default registry."""
    default_registry.register(name, strategy_func)


def get_strategy(name: str) -> Callable:
    """Get a strategy from the default registry."""
    return default_registry.get(name)


def execute_strategy(name: str, workflow: Workflow, data: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a strategy from the default registry."""
    strategy = get_strategy(name)
    return strategy(workflow, data)
