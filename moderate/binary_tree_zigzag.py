# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            
            return None
        
        levels = defaultdict(list)
        
        def dfs(root, level): 
            if root:
                levels[level].append(root.val) 
                
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        
        dfs(root, 0) 
        
        max_level = max(levels.keys())
        
        for i in range(max_level + 1):
            if i % 2 != 0:
                levels[i] = levels[i][::-1]
                
        
        return [vals for vals in levels.values()]
