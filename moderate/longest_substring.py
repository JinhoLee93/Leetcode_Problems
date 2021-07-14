class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        count = 0

        for char in s:
            if char not in chars:
                chars[char] = 0
                count += 1
            
            else:
                count -= 1
            
        return count
