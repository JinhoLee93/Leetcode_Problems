class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(palindrome) < r - l + 1:
                        palindrome = s[l:r + 1]
                
                else:
                    break
                
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(palindrome) < r - l + 1:
                        palindrome = s[l:r + 1]
                    
                else:
                    break
                
                l -= 1
                r += 1
            
            
        return palindrome
