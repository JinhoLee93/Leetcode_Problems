class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a)
        b = int(b)
        
        ab = [str(i) for i in str(a+b)]
        
        while True:
            
