"""Monte Carlo Tree Search strategy for AgenticFlow framework."""

import random
import math
from typing import Dict, Any, List, Optional, Tuple
import networkx as nx
from ..core.workflow import Workflow


class MCTSNode:
    """Node in the Monte Carlo Tree Search."""
    
    def __init__(self, context_id: str, parent=None):
        """Initialize a MCTS node."""
        self.context_id = context_id
        self.parent = parent
        self.children: List[MCTSNode] = []
        self.visits = 0
        self.value = 0.0
        self.untried_actions: List[str] = []
        
    def add_child(self, context_id: str) -> 'MCTSNode':
        """Add a child node."""
        child = MCTSNode(context_id, self)
        self.children.append(child)
        return child
    
    def update(self, result: float) -> None:
        """Update node statistics."""
        self.visits += 1
        self.value += result
        
    def uct_select_child(self, exploration_weight: float = 1.0) -> 'MCTSNode':
        """Select a child using UCT formula."""
        log_n_visits = math.log(self.visits) if self.visits > 0 else 0
        
        def uct_score(node):
            exploitation = node.value / node.visits if node.visits > 0 else 0
            exploration = exploration_weight * math.sqrt(log_n_visits / node.visits) if node.visits > 0 else float('inf')
            return exploitation + exploration
        
        return max(self.children, key=uct_score)
    
    def is_fully_expanded(self) -> bool:
        """Check if all possible actions have been tried."""
        return len(self.untried_actions) == 0
    
    def best_child(self) -> 'MCTSNode':
        """Return the best child based on value."""
        return max(self.children, key=lambda c: c.value / c.visits if c.visits > 0 else 0)


def mcts_strategy(workflow: Workflow, data: Dict[str, Any], iterations: int = 100) -> Dict[str, Any]:
    """Execute a workflow using Monte Carlo Tree Search strategy.
    
    This strategy uses MCTS to find the optimal path through the workflow graph.
    """
    # Get start contexts
    start_contexts = workflow.get_start_contexts()
    if not start_contexts:
        raise ValueError("Workflow has no start contexts")
    
    # Initialize the root node with the first start context
    root = MCTSNode(start_contexts[0].id)
    
    # Initialize untried actions for the root node
    root.untried_actions = list(workflow.graph.successors(root.context_id))
    
    # Run MCTS iterations
    for _ in range(iterations):
        # Selection
        node = _select(root, workflow)
        
        # Expansion
        if node.untried_actions:
            node = _expand(node, workflow)
        
        # Simulation
        result = _simulate(node, workflow)
        
        # Backpropagation
        _backpropagate(node, result)
    
    # Execute the best path found by MCTS
    return _execute_best_path(root, workflow, data)


def _select(node: MCTSNode, workflow: Workflow) -> MCTSNode:
    """Select a node to expand."""
    while node.is_fully_expanded() and node.children:
        node = node.uct_select_child()
        # Update untried actions for the selected node
        if not node.untried_actions:
            node.untried_actions = list(workflow.graph.successors(node.context_id))
    return node


def _expand(node: MCTSNode, workflow: Workflow) -> MCTSNode:
    """Expand a node by adding a child."""
    if not node.untried_actions:
        return node
    
    # Choose a random untried action
    action = random.choice(node.untried_actions)
    node.untried_actions.remove(action)
    
    # Add a child node
    child = node.add_child(action)
    child.untried_actions = list(workflow.graph.successors(action))
    
    return child


def _simulate(node: MCTSNode, workflow: Workflow) -> float:
    """Simulate a random playout from the given node."""
    current_id = node.context_id
    depth = 0
    max_depth = 10  # Prevent infinite loops
    
    # Simulate until we reach an end node or max depth
    while depth < max_depth:
        # Get next possible contexts
        next_ids = list(workflow.graph.successors(current_id))
        
        # If no next contexts, we've reached an end node
        if not next_ids:
            break
            
        # Choose a random next context
        current_id = random.choice(next_ids)
        depth += 1
    
    # Simple reward function: inverse of depth (shorter paths are better)
    return 1.0 / (depth + 1) if depth > 0 else 1.0


def _backpropagate(node: MCTSNode, result: float) -> None:
    """Backpropagate the result up the tree."""
    while node:
        node.update(result)
        node = node.parent


def _execute_best_path(root: MCTSNode, workflow: Workflow, data: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the best path found by MCTS."""
    from ..core.action_model import ActionModel
    action_model = ActionModel()
    
    # Start with the root node
    current_node = root
    visited = set()
    
    # Execute contexts along the best path
    while current_node and current_node.context_id not in visited:
        # Mark as visited
        visited.add(current_node.context_id)
        
        # Execute the context
        context = workflow.contexts[current_node.context_id]
        data = action_model.execute_context(context, data)
        
        # Move to the best child if any
        if current_node.children:
            current_node = current_node.best_child()
        else:
            # No more children, try to get next contexts from the workflow
            next_contexts = workflow.get_next_contexts(current_node.context_id)
            if next_contexts:
                # Create a new node for the first next context
                current_node = MCTSNode(next_contexts[0].id)
            else:
                # No more contexts to execute
                current_node = None
    
    return data
