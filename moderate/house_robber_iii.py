# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        return max(self.travel(root))
        
    def travel(self, root):
        if root == None:
            
            # With root, without root
            return [0, 0]
        
        left = self.travel(root.left)
        right = self.travel(root.right)
        
        rootBank = root.val + left[1] + right[1]
        noRootBank = max(left) + max(right)
        
        return [rootBank, noRootBank]
