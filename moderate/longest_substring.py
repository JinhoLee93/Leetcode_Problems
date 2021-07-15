class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = deque()
        win1 = 0 
        win2 = 0
        maximum = 0
        
        for char in s: 
            if char not in chars:
                chars.append(char)
                maximum = max(maximum, win1 - win2 + 1)
                win1 += 1
            
            else:
                while char in chars:
                    chars.popleft()
                    win2 += 1
        
        return maximum
