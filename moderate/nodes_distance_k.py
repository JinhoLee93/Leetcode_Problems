# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
                
            if child.left:
                dfs(child, child.left)
            
            if child.right:
                dfs(child, child.right)
        
        dfs(None, root)
        
        res = [target.val]
        visited = set(res) 
        
        for i in range(k):
            new = []
            for node in res:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new.append(neighbor)
                        visited.add(neighbor)
            
            res = new
            visited |= set(res)
        
        return res
