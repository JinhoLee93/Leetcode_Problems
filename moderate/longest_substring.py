class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = deque()
        win = 0
        maximum = 0
        
        for i in range(len(s)): 
            while s[i] in chars:
                chars.popleft()
                win += 1
            
            chars.append(s[i])
            maximum = max(maximum, i - win + 1)
            
        return maximum
