# Runtime: 24 ms, Memory usage: 14.2 MB
# Easy Stack implementation
class Solution:
    def isValid(self, s: str) -> bool:
        pa = [str(i) for i in str(s)] 
        stack = list()
        
        for i in pa:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            
            elif i == ')' or i == ']' or i == '}':
                                    
                if len(stack) < 1:
                    return False
                
                if i == ')':
                    if stack[-1] == '(': 
                        stack.pop()
                        
                    else:
                        return False
                    
                if i == ']':
                    if stack[-1] == '[':
                        stack.pop() 
                    
                    else:
                        return False
                
                if i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                        
                    else: 
                        return False


        if len(stack) == 0:
            return True 
        
        else:
            return False
