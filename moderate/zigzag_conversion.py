class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        mat = [[] for i in range(numRows)]
        rev = False
        res = ""
        
        i = -1
        c = 0
        for char in s:
            if not rev: 
                if i == (numRows - 1):
                    rev = True
                    i -= 1
                    mat[i].append(char)

                else:
                    i += 1
                    mat[i].append(char)

            else:
                if i == 0:
                    rev = False
                    i += 1
                    mat[i].append(char)

                else:
                    i -= 1
                    mat[i].append(char)

        for i in range(numRows):
            for j in range(len(mat[i])):
                res += mat[i][j]
                
        return res
