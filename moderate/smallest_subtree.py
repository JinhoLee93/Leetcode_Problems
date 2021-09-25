# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = defaultdict(TreeNode)
        
        def dfs(root, dep):
            if root:
                depth[root] = dep
                
                dfs(root.left, dep + 1) 
                dfs(root.right, dep + 1)
        
        dfs(root, 0)
        
        max_depth = max(depth.values())
        
        def find(root):
            if not root or depth[root] == max_depth: 
                
                return root
            
            left, right = find(root.left), find(root.right)
                
            return root if left and right else left or right
        
        return find(root)
