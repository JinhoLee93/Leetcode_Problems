# Runtime: 12 ms (Faster than 100%) Space: 14.2 MB
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        paren = []
        
        for c in s:
            if c in hashmap:
                if len(paren) == 0:
                    
                    return False 
                
                if paren[-1] == hashmap[c]:
                    paren.pop()
                
                else:
                    
                    return False
            
            else:
                paren.append(c)
            
        
        return True if len(paren) == 0 else False
