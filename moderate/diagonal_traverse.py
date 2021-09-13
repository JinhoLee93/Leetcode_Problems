class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0:
            
            return []
        
        ROWS, COLS = len(mat), len(mat[0])
        result = [0] * (ROWS * COLS)
        
        r = c = 0
        for i in range(len(result)):
            result[i] = mat[r][c]
            if (r + c) % 2 == 0:
                if c == COLS - 1:
                    r += 1

                elif r == 0:
                    c += 1

                else:
                    r -= 1
                    c += 1

            else:
                if r == ROWS - 1:
                    c += 1
                
                elif c == 0:
                    r += 1
                
                else:
                    r += 1
                    c -= 1
                    
        return result
