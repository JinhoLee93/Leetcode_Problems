# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res 
            
            if not root:
                
                return float('inf'), float('-inf'), 0
            
            lmin, lmax, lnum = dfs(root.left)
            rmin, rmax, rnum = dfs(root.right)
            
            cur = float('-inf')
            if lmax < root.val and rmin > root.val:
                cur = lnum + rnum + 1
                res = max(res, cur)
                
            return min(lmin, root.val), max(rmax, root.val), cur
        
        dfs(root)
        
        return res
