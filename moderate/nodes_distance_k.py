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
        
        bfs = [target.val]
        visited = set(bfs)
        
        for i in range(k):
            new = []
            
            for node in bfs:
                for connected in graph[node]:
                    if connected not in visited:
                        new.append(connected)
            
            bfs = new
            visited |= set(bfs)
            
        return bfs
