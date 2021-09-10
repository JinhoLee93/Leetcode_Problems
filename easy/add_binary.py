class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        res = ""
        
        for i in range(n - 1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                if carry > 0:
                    res += '1'
                    carry -= 1
                
                else:
                    res += '0'
            
            elif a[i] == '1' and b[i] == '0':
                if carry > 0:
                    res += '0'
                    
                else:
                    res += '1'
            
            elif a[i] == '0' and b[i] == '1':
                if carry > 0:
                    res += '0'
                
                else:
                    res += '1'
            
            elif a[i] == '1' and b[i] == '1':
                if carry > 0:
                    res += '1'
                
                else:
                    res += '0'
                    carry += 1
                
        if carry == 1:
            res += str(carry)
        
        return res[::-1]
