# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def postorder(root, res): 
            if root is not None:
                postorder(root.left, res)
                postorder(root.right, res)
                
                res.append(root.val)
        
        postorder(root, res)
        
        return res
