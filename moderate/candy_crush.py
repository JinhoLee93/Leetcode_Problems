class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Time: O((R*C)^2), Space: O(R+C)
        ROWS, COLS = len(board), len(board[0]) 
        pathSet = set()
        
        def checkDown(r, c, val, i):
            if r > (ROWS - 1) or \
                board[r][c] != val:
                
                return i
            
            rows.append((r, c))
            
            return checkDown(r + 1, c, val, i + 1)
        
        def checkRight(r, c, val, i):
            if c > (COLS - 1) or \
                board[r][c] != val:
                
                return i 
            
            cols.append((r, c))
            
            return checkRight(r, c + 1, val, i + 1)
            
        
        while True:
            # Crush
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == 0: 
                        continue 
                    
                    rows = []
                    cols = []
                    rowDown = checkDown(r, c, board[r][c], 0)
                    colRight = checkRight(r, c, board[r][c], 0)
                    
                    if rowDown > 2:
                        for cell in rows:
                            pathSet.add(cell)
                            
                    if colRight > 2:
                        for cell in cols:
                            pathSet.add(cell)
            
            if len(pathSet) == 0:
                
                break 
            
            for r in range(ROWS):
                for c in range(COLS):
                    if (r, c) in pathSet: 
                        for i in range(r, 0, -1):
                            board[i][c] = board[i - 1][c]

                        board[0][c] = 0
                        pathSet.remove((r, c))
                            
        return board
