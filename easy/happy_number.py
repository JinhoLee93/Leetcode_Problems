# Faster than 100%
class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        
        while n != 1:
            res = 0
            n = str(n)
            
            for i in range(len(n)):
                res += int(n[i]) ** 2

            if res not in cycle:
                cycle.add(res)
                n = res
            
            else:
                return False
            
        return True
