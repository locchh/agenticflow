"""Breadth-First Search strategy for AgenticFlow framework."""

from typing import Dict, Any, Set, Deque
from collections import deque
from ..core.workflow import Workflow


def bfs_strategy(workflow: Workflow, data: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a workflow using Breadth-First Search strategy.
    
    This strategy traverses the workflow graph breadth-first, executing all contexts
    at the same level before moving to the next level.
    """
    # Get start contexts
    start_contexts = workflow.get_start_contexts()
    if not start_contexts:
        raise ValueError("Workflow has no start contexts")
    
    # Initialize queue with start contexts
    queue = deque([(ctx.id, data) for ctx in start_contexts])
    visited = set()
    
    # Process queue
    while queue:
        context_id, current_data = queue.popleft()
        
        # Skip if already visited
        if context_id in visited:
            continue
            
        # Mark as visited
        visited.add(context_id)
        
        # Get the context
        context = workflow.contexts[context_id]
        
        # Execute the context
        from ..core.action_model import ActionModel
        action_model = ActionModel()
        updated_data = action_model.execute_context(context, current_data.copy())
        
        # Get next contexts and add to queue
        next_contexts = workflow.get_next_contexts(context_id)
        for next_context in next_contexts:
            if next_context.id not in visited:
                queue.append((next_context.id, updated_data))
    
    return data
