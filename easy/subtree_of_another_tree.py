# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None and subRoot == None:
            
            return True 
        
        elif root == None or subRoot == None:
            
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or \
            self.isTree(root, subRoot)
    
    def isTree(self, root, subRoot):
        if root == None and subRoot == None:
            
            return True 
        
        elif root == None or subRoot == None:
            
            return False
        
        return root.val == subRoot.val and self.isTree(root.left, subRoot.left) and \
            self.isTree(root.right, subRoot.right)
