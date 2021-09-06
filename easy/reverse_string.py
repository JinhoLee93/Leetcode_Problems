class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # API
        s = s.reverse()
        
        # Two Pointers
        l, r = 0, len(s) - 1
        while l <= r: 
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp
            
            l += 1
            r -= 1
