class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window1, window2 = 0, 0
        seen = {}
        maxLength = 0
                
        for idx, char in enumerate(s):
            if char in seen and window1 <= seen[char]:
                window1 = seen[char] + 1
            
            maxLength = max(maxLength, idx - window1 + 1)
            seen[char] = idx
            
        return maxLength
