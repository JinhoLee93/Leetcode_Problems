class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        shouldDie, shouldLive = [], []
        
        def check(r, c):
            if r < 0 or c < 0 or \
                r > ROWS - 1 or c > COLS - 1:
                
                return False
            
            if board[r][c] == 0:
                
                return False
            
            elif board[r][c] == 1:
                
                return True
            
        for r in range(ROWS):
            for c in range(COLS):
                neighbors = check(r + 1, c) + check(r - 1, c) + check(r, c + 1) + check(r, c - 1) + \
                            check(r + 1, c + 1) + check(r + 1, c - 1) + check(r - 1, c + 1) + check(r - 1, c - 1)
                
                if board[r][c] == 1 and neighbors > 3:
                    shouldDie.append((r, c))
                
                elif board[r][c] == 1 and neighbors < 2:
                    shouldDie.append((r, c))
                
                if board[r][c] == 0 and neighbors == 3:
                    shouldLive.append((r, c))

        
        for r, c in shouldDie:
            board[r][c] = 0
        
        for r, c in shouldLive:
            board[r][c] = 1
        
