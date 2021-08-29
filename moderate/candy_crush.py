class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(board), len(board[0])
        pathSet = set() 
        
        def rowCheck(r, c, prv, rowArr):
            if r > ROWS - 1 or \
                board[r][c] != prv:
                
                return 0
            
            rowArr.append((r, c))
            
            return rowCheck(r + 1, c, board[r][c], rowArr) + 1
        
        def colCheck(r, c, prv, colArr):
            if c > COLS - 1 or \
                board[r][c] != prv:
                
                return 0
            
            colArr.append((r, c))
            
            return colCheck(r, c + 1, board[r][c], colArr) + 1
            
        while True:
            # Crush
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] != 0:
                        rows = []
                        cols = []

                        if rowCheck(r, c, board[r][c], rows) > 2:
                            for i in range(len(rows)):
                                pathSet.add(rows[i])

                        if colCheck(r, c, board[r][c], cols) > 2:
                            for i in range(len(cols)):
                                pathSet.add(cols[i])
                            
            if len(pathSet) == 0:
                
                break
            
            # Refill
            for r in range(ROWS):
                for c in range(COLS):
                    if (r, c) in pathSet:
                        for i in range(r, 0, -1):
                            board[i][c] = board[i - 1][c]
                            
                        board[0][c] = 0
            
            pathSet.clear()
        
        return board
