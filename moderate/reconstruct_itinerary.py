class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itis = {fr: [] for fr, to in tickets}
        for fr, to in tickets:
            itis[fr].append(to)
            if to not in itis:
                itis[to] = []
        
        for key in itis.keys():
            itis[key].sort(reverse=True)
        
        newIti = []
        pathSet = set()
    
        def dfs(airport):
            while itis[airport]:
                nxt = itis[airport].pop()
                dfs(nxt)
            newIti.append(airport)
            
        dfs("JFK")
        
        return newIti[::-1]
