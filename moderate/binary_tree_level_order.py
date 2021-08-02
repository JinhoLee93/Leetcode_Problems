# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return [] 
        
        q = deque() 
        q.append(root)
        level = 0
        
        while q:
            level += 1
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
                    
        res = [[] for i in range(level)]
        
        def dfs(root, res, level):
            if root == None:
                return None
            
            res[level].append(root.val)
            
            dfs(root.left, res, level + 1)
            dfs(root.right, res, level + 1)
            
        dfs(root, res, 0)
        
        return res
