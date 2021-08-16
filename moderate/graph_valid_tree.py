class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time: O(E(number of edges) + V(number of vertices)), Space: O(E + V)
        adj = {i:[] for i in range(n)}
        visitSet = set()
        
        for root, child in edges:
            adj[root].append(child)
            adj[child].append(root)
            
            
        def dfs(root, prv):
            if root in visitSet:
                
                return False
            
            visitSet.add(root)
            
            for child in adj[root]:
                if child == prv:
                    continue
                
                if not dfs(child, root):
                    return False
                
            return True
        
        return dfs(0, -1) and n == len(visitSet)
