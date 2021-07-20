# Runtime: 24 ms, Memory usage: 14 MB
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        chars = list(string.ascii_uppercase)
        
        while n > 0:
            res += chars[(n - 1) % 26]
            n = (n - 1) // 26
            
        return res[::-1]
