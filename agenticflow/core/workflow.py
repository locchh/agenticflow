"""Workflow module for AgenticFlow framework.

This module defines the Workflow class which represents a workflow of contexts.
A workflow can be structured as a chain, tree, or graph of contexts.
"""

import networkx as nx
from typing import Dict, List, Any, Optional, Set
from .context import Context


class Workflow:
    """A workflow of contexts.
    
    A workflow is structured as a chain, tree, or graph of contexts.
    """
    
    def __init__(self, name: str, description: str = ""):
        """Initialize a workflow."""
        self.name = name
        self.description = description
        self.graph = nx.DiGraph()
        self.contexts: Dict[str, Context] = {}
        
    def add_context(self, context: Context) -> None:
        """Add a context to the workflow."""
        if context.id in self.contexts:
            raise ValueError(f"Context with id {context.id} already exists in workflow")
        
        self.contexts[context.id] = context
        self.graph.add_node(context.id)
        
    def connect(self, from_context_id: str, to_context_id: str, condition: Optional[str] = None) -> None:
        """Connect two contexts in the workflow."""
        if from_context_id not in self.contexts:
            raise ValueError(f"Context with id {from_context_id} does not exist in workflow")
        if to_context_id not in self.contexts:
            raise ValueError(f"Context with id {to_context_id} does not exist in workflow")
        
        # Add edge with optional condition
        self.graph.add_edge(from_context_id, to_context_id, condition=condition)
        
    def get_next_contexts(self, context_id: str) -> List[Context]:
        """Get the next contexts after the given context."""
        if context_id not in self.contexts:
            raise ValueError(f"Context with id {context_id} does not exist in workflow")
        
        next_context_ids = list(self.graph.successors(context_id))
        return [self.contexts[ctx_id] for ctx_id in next_context_ids]
    
    def get_start_contexts(self) -> List[Context]:
        """Get all starting contexts (those with no predecessors)."""
        start_nodes = [n for n in self.graph.nodes if self.graph.in_degree(n) == 0]
        return [self.contexts[ctx_id] for ctx_id in start_nodes]
    
    def get_end_contexts(self) -> List[Context]:
        """Get all ending contexts (those with no successors)."""
        end_nodes = [n for n in self.graph.nodes if self.graph.out_degree(n) == 0]
        return [self.contexts[ctx_id] for ctx_id in end_nodes]
    
    def visualize(self, filename: str = None) -> None:
        """Visualize the workflow graph."""
        try:
            import matplotlib.pyplot as plt
            
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(self.graph)
            
            # Draw nodes
            nx.draw_networkx_nodes(self.graph, pos, node_size=700)
            
            # Draw edges
            nx.draw_networkx_edges(self.graph, pos, arrowsize=20)
            
            # Draw labels
            labels = {ctx_id: self.contexts[ctx_id].name for ctx_id in self.graph.nodes}
            nx.draw_networkx_labels(self.graph, pos, labels=labels)
            
            # Draw edge labels (conditions)
            edge_labels = {(u, v): d.get('condition', '') 
                          for u, v, d in self.graph.edges(data=True) 
                          if d.get('condition')}
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
            
            plt.title(f"Workflow: {self.name}")
            plt.axis('off')
            
            if filename:
                plt.savefig(filename)
            else:
                plt.show()
                
        except ImportError:
            print("Matplotlib is required for visualization")
            
    def __str__(self) -> str:
        return f"Workflow({self.name}, {len(self.contexts)} contexts)"
    
    def __repr__(self) -> str:
        return self.__str__()
