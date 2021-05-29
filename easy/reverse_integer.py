# Runtime: 28 ms, Memory usage: 14.3 MB
class Solution:
    def reverse(self, x: int) -> int:
        digits = list(str(x))
        digits = digits[::-1]
        
        # edge case #1 (If the given number is negative, the result shouldn't reverse the sign.)
        if x < 0:
            temp = digits[len(digits) - 1]
            digits.pop()
            digits.insert(0, temp)
                
        digit = str()
        
        for i in range(len(digits)):
            digit += digits[i]
        
        digit = int(digit)
        
        # edge case #2 (The digit must be bigger than -2^31 or smaller than 2^31 - 1.)
        if digit < (-2)**31 or digit > (2**31 - 1):
            digit = 0
            
            
        return digit
