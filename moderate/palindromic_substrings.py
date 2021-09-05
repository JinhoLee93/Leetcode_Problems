class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Time: O(N^2) Space: O(N^2) 
        def lps(original, reverse):
            dp = [[0 for i in range(len(reverse) + 1)] for j in range(len(original) + 1)]
            
            for r in range(len(original) - 1, -1, -1):
                for c in range(len(reverse) - 1, -1, -1):
                    if original[r] == reverse[c]:
                        dp[r][c] = 1 + dp[r + 1][c + 1]
                    
                    else:
                        dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
            
            return dp[0][0]
        
        return lps(s, s[::-1])
                        
