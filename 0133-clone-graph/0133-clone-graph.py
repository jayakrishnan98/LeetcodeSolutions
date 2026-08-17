"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewMap = {}

        def clone(node):
            if node in oldToNewMap:
                return oldToNewMap[node]

            copy = Node(node.val)
            oldToNewMap[node] = copy

            for neighbour in node.neighbors:
                copy.neighbors.append(clone(neighbour))
            return copy
            
        return clone(node) if node else None