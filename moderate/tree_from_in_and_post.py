# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            
            return None 
        
        root = TreeNode(postorder[-1])
        
        in_root_idx = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[0:in_root_idx], postorder[0:in_root_idx])
        root.right = self.buildTree(inorder[in_root_idx + 1:len(inorder)], postorder[in_root_idx:len(postorder) - 1])
         
        return root
