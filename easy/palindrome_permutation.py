class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        length = len(s)
        
        if length % 2 == 0:
            for val in count.values():
                if val % 2 != 0:
                    
                    return False
            
        else:
            left = 1
            for val in count.values():
                if val % 2 == 1 and left < 1:
                    
                    return False
                
                elif val % 2 == 1 and left == 1:
                    
                    left -= 1
                
        return True
