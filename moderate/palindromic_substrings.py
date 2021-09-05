class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(N^2), Space: O(N)
        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            dp[i] = 1
            for j in range(i - 1, -1, -1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i - j] += 1
        

        return sum(dp)
