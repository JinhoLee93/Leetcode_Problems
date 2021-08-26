class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in seen and window1 <= seen[s[r]]:
                l = seen[s[r]] + 1    
                
            seen[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
