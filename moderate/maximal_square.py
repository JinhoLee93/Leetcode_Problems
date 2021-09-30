class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[0 for i in range(COLS)] for i in range(ROWS)]
        area = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == '0':
                    cache[r][c] = 0
                    continue
                
                else:
                    cache[r][c] = 1

                if (r + 1 < ROWS) and (c + 1 < COLS) and cache[r][c] == 1:
                    right, down, diag = cache[r][c + 1], cache[r + 1][c], cache[r + 1][c + 1]
                    
                    if right == 0 or down == 0 or diag == 0:
                        cache[r][c] = 1
                    
                    elif right == down == diag:
                        cache[r][c] = diag + 1
                    
                    else:
                        cache[r][c] = min(right, down, diag) + 1
                        
                area = max(area, cache[r][c])
        
        return area ** 2
