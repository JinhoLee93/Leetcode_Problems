# Faster than 100%
class Solution:
    def trailingZeroes(self, n: int) -> int:
        denom = 5
        res = 0
        while denom <= n:
            res += n//denom
            denom *= 5
        
        return res
