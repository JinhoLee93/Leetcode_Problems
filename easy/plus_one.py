# Runtime: 42 ms, Memory usage: 14 MB
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i)) 
        
        num += 1
        
        nums = [int(str(i)) for i in str(num)]
        
        return nums
