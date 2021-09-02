class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Time: O(R * C) Space: O(R * C)
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        pathSet = set() 
        uniqueList = []
        
        def dfs(r, c):
            nonlocal arr
            
            if r < 0 or c < 0 or \
                r > ROWS - 1 or c > COLS - 1 or \
                (r, c) in pathSet or \
                board[r][c] != "O":
                
                return 
            
            pathSet.add((r, c))
            arr.append((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in pathSet and board[r][c] == "O":
                    border = False
                    arr = []
                    dfs(r, c)

                    for i, j in arr:
                        if i == ROWS - 1 or i == 0 or \
                            j == COLS - 1 or j == 0:
                            border = True
                    
                    if not border:
                        for i, j in arr:
                            board[i][j] = "X"
