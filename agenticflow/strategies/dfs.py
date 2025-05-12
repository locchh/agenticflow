"""Depth-First Search strategy for AgenticFlow framework."""

from typing import Dict, Any, Set
from ..core.workflow import Workflow


def dfs_strategy(workflow: Workflow, data: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a workflow using Depth-First Search strategy.
    
    This strategy traverses the workflow graph depth-first, executing each context
    and following the first available path until reaching an end context.
    """
    # Get start contexts
    start_contexts = workflow.get_start_contexts()
    if not start_contexts:
        raise ValueError("Workflow has no start contexts")
    
    # Track visited contexts to avoid cycles
    visited = set()
    
    # Execute DFS from each start context
    for start_context in start_contexts:
        data = _dfs_execute(workflow, start_context.id, data, visited)
    
    return data


def _dfs_execute(workflow: Workflow, context_id: str, data: Dict[str, Any], visited: Set[str]) -> Dict[str, Any]:
    """Recursively execute contexts in depth-first order."""
    # Skip if already visited
    if context_id in visited:
        return data
    
    # Mark as visited
    visited.add(context_id)
    
    # Get the context
    context = workflow.contexts[context_id]
    
    # Execute the context
    from ..core.action_model import ActionModel
    action_model = ActionModel()
    data = action_model.execute_context(context, data)
    
    # Get next contexts
    next_contexts = workflow.get_next_contexts(context_id)
    
    # Execute each next context
    for next_context in next_contexts:
        data = _dfs_execute(workflow, next_context.id, data, visited)
    
    return data
