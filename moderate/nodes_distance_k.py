# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        res = []
        
        # Make a graph with DFS
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
        
        for _ in range(k):
            new = []
            
            for node in bfs:
                for undirected in graph[node]:
                    if undirected not in visited:
                        new.append(undirected)
                        visited.add(undirected)
                        
            bfs = new
            
        return bfs
