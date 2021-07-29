# Solution conceived by YouTuber NeetCode (https://www.youtube.com/watch?v=XYQecbcd6_c&t=173s&ab_channel=NeetCode)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = "" 
        anslen = 0 
        
        for i in range(len(s)): 
            r, l = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]: 
                if r - l + 1 > anslen:
                    ans = s[l:r+1]
                    anslen = r - l + 1
                l -= 1
                r += 1
            
            r, l = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]: 
                if r - l + 1 > anslen:
                    ans = s[l:r+1]
                    anslen = r - l + 1
                l -= 1
                r += 1
                
        return ans
