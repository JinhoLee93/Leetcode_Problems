# Runtime: 48 ms, Memory usage: 14.6 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                string += s[i]
        
        if string == string[::-1]: 
            return True
        
        return False
