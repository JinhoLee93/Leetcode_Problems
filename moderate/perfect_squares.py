class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                square = j ** 2 
                
                if i - square < 0:
                    break
                
                if dp[i] > dp[i - square] + 1:
                    dp[i] = dp[i - square] + 1
                    
        return dp[n]
