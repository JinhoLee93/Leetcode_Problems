# Runtime: 32 ms, Memory usage: 14.2 MB
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        
        # Solving pesky edge cases
        while True: 
            if words[len(words) - 1] == '' and len(words) > 1:
                words.pop()
            else:
                break
                
        return len(words[len(words) - 1])
