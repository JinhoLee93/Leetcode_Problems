class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            
            return board
            
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        def dfs(r, c):
            if board[r][c] != 'E' or \
                (r, c) in visited:
                
                return

            visited.add((r, c))
            mines = 0
            for move in moves:
                nxtR, nxtC = r + move[0], c + move[1]
                if 0 <= nxtR < ROWS and 0 <= nxtC < COLS and board[nxtR][nxtC] == 'M':
                    mines += 1
                    
            if mines == 0:
                board[r][c] = 'B'
            
            else:
                board[r][c] =  str(mines)
                
            if not board[r][c].isdigit():
                for move in moves:
                    nxtR, nxtC = r + move[0], c + move[1]
                    if 0 <= nxtR < ROWS and 0 <= nxtC < COLS:
                        dfs(nxtR, nxtC)
            
        dfs(click[0], click[1])
                
        return board
