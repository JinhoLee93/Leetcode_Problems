# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None:
            
            return False
        
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)
    
def is_same(root, subRoot):
    if root == None and subRoot == None:
        
        return True
    
    if root and subRoot:
        
        return root.val == subRoot.val and is_same(root.left, subRoot.left) and \
                is_same(root.right, subRoot.right)
    
    return False
