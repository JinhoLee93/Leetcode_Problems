class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time: O(E + V), Space: O(E + V)
        adj = {i: [] for i in range(n)}
        pathSet = set()
        count = 0
        
        for vertex, adjacent in edges:
            adj[vertex].append(adjacent)
            adj[adjacent].append(vertex)
        
        def dfs(root, prv):
            if root in pathSet:
                
                return
            
            pathSet.add(root)
            
            for vertex in adj[root]:
                if prv == vertex:
                    continue
                    
                else:
                    dfs(vertex, root)
                
            return
        
        for root in adj:
            if root not in pathSet:
                dfs(root, -1)
                count += 1
            
        return count
        
