class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time: O(N * M), Space: O(N + M)
        ROWS, COLS = len(text1), len(text2)
        
        dp = [[0 for i in range(COLS + 1)] for j in range(ROWS + 1)] 
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                else: 
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    
        
        return dp[0][0]
