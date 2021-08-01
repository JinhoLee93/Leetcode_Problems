class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            res[i] = str(bin(i)[2:]).count("1")
            
        return res
    
# DP
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
                
            res[i] = 1 + res[i - offset]
            
        return res
            
