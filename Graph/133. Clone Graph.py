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
        if not node:
            return
        
        visit={}
        
        def dfs(node):
            if node in visit:
                return visit[node]
            
            clone=Node(node.val)
            visit[node]=clone
            
            
            for i in node.neighbors:
                
                clone.neighbors.append(dfs(i))
                
            return clone
        
        return dfs(node)