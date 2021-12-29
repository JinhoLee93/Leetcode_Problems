class Solution:
    def reverse(self, x: int) -> int:
        rev, res, neg = 0, "", False
        x = list(str(x))
        
        if x[0] == '0':
            
            return 0
        
        if x[0] == '-':
            neg = True
            x.reverse()
            x.pop()   
        
        else:
            x.reverse()
            
        i = 0
        while x[i] == '0':
            i += 1
        
        for j in range(i, len(x)):
            res += x[j]
        
        if neg:
            res = "-" + res
        
        res = int(res)
                
        if -2 ** 31 < res < 2 ** 31 - 1:
    
            return res
    
        return 0
        
