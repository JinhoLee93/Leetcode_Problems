# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        res = []
        
        def dfs(root, level):
            if root:
                levels[level].append(root.val)
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
                
        dfs(root, 0)
        
        for i in range(len(levels)):
            res.append(levels[i][-1])
        
        return res
