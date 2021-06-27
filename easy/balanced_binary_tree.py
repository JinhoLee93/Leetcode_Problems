# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root): 
        if root == None: 
            return -1
        
        return max(self.check(root.left), self.check(root.right)) + 1
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None: 
            return True
        
        else: 
            if self.isBalanced(root.left) == False:
                return False 
            
            if self.isBalanced(root.right) == False:
                return False 
            
            left_height = self.check(root.left)
            right_height = self.check(root.right)
            
            return abs(left_height - right_height) < 2
