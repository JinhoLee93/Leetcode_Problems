# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    # Space: O(1), Time: O(N)
        res = 0
        
        def dfs(root, floor):
            nonlocal res
            
            if not root:
                
                return
            
            if root.val >= floor:
                res += 1
                right = dfs(root.right, root.val)
                left = dfs(root.left, root.val)
                
            else:
                right = dfs(root.right, floor)
                left = dfs(root.left, floor)
        
        dfs(root, root.val)
        
        return res
