# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        else:
            return []
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        one = self.inorder(p)
        two = self.inorder(q)
        
        print(one, two)
        
        if one == two:
            return True
        else:
            return False
