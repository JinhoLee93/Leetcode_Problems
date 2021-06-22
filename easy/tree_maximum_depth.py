# Runtime: 36 ms, Memory usage: 16 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: 
            return 0
        
        ld = self.maxDepth(root.left) + 1
        rd = self.maxDepth(root.right) + 1
        
        return max(ld, rd)
