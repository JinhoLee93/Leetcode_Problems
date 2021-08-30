# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root:
                
                return [False, False]
            
            left, lFound = dfs(root.left, p, q)
            right, rFound = dfs(root.right, p, q)
            cur = root.val == p.val or root.val == q.val
            
            if (cur and left) or (cur and right) or (left and right):
                
                return [root, True]
            
            return [left or right or cur, lFound or rFound]
        
        root, found = dfs(root, p, q)
        
        if not found:
            
            return None
        
        return root
