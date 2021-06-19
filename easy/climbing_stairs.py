class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        if n == 0: 
            return dp[0]    
        elif n == 1:
            return dp[1]
        
        for i in range(n + 1):
            if i > 1:
                dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
