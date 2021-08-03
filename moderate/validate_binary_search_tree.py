# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(floor, ceil, root):
            if root == None:
                
                return True 
            
            if not (root.val < ceil and root.val > floor):
                
                return False 
                
            return check(floor, root.val, root.left) and check(root.val, ceil, root.right)
            
        
        return check(float('-inf'), float('inf'), root)
