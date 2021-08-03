# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        #preorder: [root.val] + self.buildTree(root.left) + self.buildTree(root.right)
        
        #inorder: self.buildTree(root.left) + [root.val] + self.buildTree(root.right)
        
        if not inorder or not preorder:
            return None
        
        root = TreeNode(preorder[0])
        in_root_idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:in_root_idx + 1], inorder[0:in_root_idx])
        root.right = self.buildTree(preorder[in_root_idx + 1: len(preorder)], inorder[in_root_idx + 1: len(inorder)])
        
        return root
