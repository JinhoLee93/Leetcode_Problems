# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root, i): 
        i += 1
        
        return self.depth(root.left, root.right, i)
    def maxDepth(self, root: TreeNode) -> int:
        i = 0
        
        
