"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Time: O(N * M), Space: O(N * M)
        nodeSet = set()
        
        def dfs(node):
            if not node:
                
                return
            
            if node in nodeSet:
                
                return node
            
            nodeSet.add(node)
            
            return dfs(node.parent)
            
            
        dfs(p)
        
        return dfs(q)
