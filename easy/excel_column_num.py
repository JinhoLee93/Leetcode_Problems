class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        chars = list(string.ascii_uppercase)
        res = 0
        
        for i in range(len(columnTitle)):
            
            res += 26 ** ((len(columnTitle) - 1) - i) * (chars.index(columnTitle[i]) + 1)
            
            
        return res
