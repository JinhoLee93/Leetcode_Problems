# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, depth):
        depth += 1
        
        if root.left == None and root.right == None:
            
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True 
        else: 
            depth_left = 1
            depth_right = 1
            
            ml = self.check(root.left, depth_left)
            mr = self.check(root.right, depth_right)
            
            if abs(ml-mr) < 1:
                return True
            else:
                return False
