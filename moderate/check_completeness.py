# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def dfs(root):
            nonlocal res
            
            if not root:
                
                return (0, 0)
            
            ll, lr = dfs(root.left)
            rl, rr = dfs(root.right)
            l, r = max(ll, lr), min(rl, rr)
            
            if not (rr <= rl <= lr <= ll and 0 <= ll - lr <= 1):
                res = False
                
            return (l + 1, r + 1)
        
        l, r = dfs(root)
        
        return res and (0 <= l - r <= 1)
