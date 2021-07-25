class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        mat = [[] for i in range(numRows)]
        rev = False
        res = ""
        
        i = 0
        for char in s:
            if not rev: 
                if i == numRows:
                    rev = True
                    i -= 2
                    mat[i].append(char)
                
                else:
                    mat[i].append(char)
                    i += 1
                
            else:
                if i == 0:
                    rev = False
                    mat[i].append(char)
                    i += 1
                    
                else:
                    i -= 1
                    mat[i].append(char)
    
        print(mat)
        return res
