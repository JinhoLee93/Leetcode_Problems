class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1) 
        res = 0 
        
        def backtrack(n, pos):
            nonlocal res
            
            if pos > n: 
                res += 1
                
            for i in range(1, n + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True 
                    backtrack(n, pos + 1)
                    visited[i] = False

        backtrack(n, 1)
        
        return res
