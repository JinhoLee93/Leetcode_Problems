
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            
            return root
        
        last, first = None, None
        
        def dfs(root):
            nonlocal last, first
            if root:
                dfs(root.left)
                if not last:
                    first = root
                
                else:
                    last.right = root
                    root.left = last
                
                last = root
                dfs(root.right)
        
        dfs(root)
        last.right = first 
        first.left = last
        
        return first
