# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self.minDepth(root.left) + 1
        right = self.minDepth(root.right) + 1
        
        if left == 1 and right > 1:
            return right
        
        if right == 1 and left > 1:
            return left
        
        return min(left, right)
