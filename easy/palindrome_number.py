class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Advanced solution without converting the integer into a string.
        # Runtime: 108 ms, Memory usage: 14.4 MB
        if x < 0:
            return False
        
        elif x >= 0 and x <= 9: 
            return True
        
        y = x
        num = 0
        while y >= 1:
            num = num * 10 + y % 10
            y = y // 10
            
        if num == x: 
            return True 
        
        else:
            return False
        
        # Solution #2 with converting the integer into a string.
        # Runtime: 76 ms, Memory usage: 14.2 MB
        """
        xlist = [str(i) for i in str(x)]
        ylist = [str(i) for i in str(x)]
        xlist.reverse()
        if xlist == ylist:
            return True
        else:
            return False
        """
        
