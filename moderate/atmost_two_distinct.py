class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
      # Time: O(N), Space: O(1)
        chars = {}
        maxLength, window = 0, 0
        
        for i in range(len(s)):
            chars[s[i]] = 1 + chars.get(s[i], 0)
            
            if len(chars) > 2:
                for j in range(window, i):
                    chars[s[j]] -= 1
                    
                    if chars[s[j]] == 0:
                        chars.pop(s[j])
                        window = j + 1
                        break
            
            maxLength = max(maxLength, sum(chars.values()))
                
        return maxLength
