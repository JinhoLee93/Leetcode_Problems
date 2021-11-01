"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            
            return root
        
        tree = {}
        
        def dfs(root):
            if not root:
                
                return root
            
            clone = Node(root.val)
            tree[root] = clone
            
            for child in root.children:
                tree[root].children.append(dfs(child))
            
            return tree[root]
        
        return dfs(root)
