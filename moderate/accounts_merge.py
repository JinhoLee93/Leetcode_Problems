class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        em2name = {}
        result = []
        visitSet = set() 
        
        # Construct a graph
        for acc in accounts:
            name, root = acc[0], acc[1]
            em2name[root] = name
            if root not in graph:
                graph[root] = []
                
            for email in acc[2:]:
                graph[root].append(email)
                graph[email].append(root)
                em2name[email] = name
                
        def dfs(email):
            nonlocal tmp
            
            if email in visitSet:
                
                return
        
            visitSet.add(email)
            tmp.append(email)
            
            for neighbor in graph[email]:
                dfs(neighbor)
        
        for email in graph:
            name = [em2name[email]]
            tmp = []
            dfs(email)
            if len(tmp) > 0:
                result.append(name + sorted(tmp))
        
        return result
