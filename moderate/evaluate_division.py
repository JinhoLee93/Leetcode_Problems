class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        eqs = defaultdict(defaultdict)
        visited = set()
        for idx, (dividend, divisor) in enumerate(equations):
            eqs[dividend][divisor] = values[idx]
            eqs[divisor][dividend] = 1 / values[idx]
            
        def dfs(dividend, divisor, prod):
            visited.add(dividend)
            ret = -1
            neighbors = eqs[dividend]
            if divisor in neighbors:
                ret = prod * neighbors[divisor]
            
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                        
                    ret = dfs(neighbor, divisor, prod * value)
                    
                    if ret != -1:
                        
                        break
            
            visited.remove(dividend)
            
            return ret
        
        for dividend, divisor in queries:
            if dividend not in eqs or divisor not in eqs:
                result.append(-1)
            
            elif dividend == divisor:
                result.append(1)
            
            else:
                result.append(dfs(dividend, divisor, 1))
        
        return result
