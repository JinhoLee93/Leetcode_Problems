class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            
            return 0 
        
        chars = {} 
        maxLength = 0
        window = 0
        
        for i in range(len(s)):
            chars[s[i]] = 1 + chars.get(s[i], 0)
            if len(chars) > k:
                for j in range(window, i):
                    chars[s[j]] -= 1
                    
                    if chars[s[j]] == 0:
                        chars.pop(s[j])
                        window = j + 1
                        break
            
            maxLength = max(maxLength, sum(chars.values()))
            
        return maxLength
