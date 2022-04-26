class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, diagNeg, diagPos = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        res = []
        
        def dfs(r):
            if r == n:
                line = ["".join(row) for row in board]
                res.append(line)
                
                return
            
            for c in range(n):
                if (r - c) in diagNeg or (r + c) in diagPos or c in col:
                    continue 
                    
                diagNeg.add(r - c)
                diagPos.add(r + c)
                col.add(c)
                board[r][c] = "Q"
                
                dfs(r + 1)
                
                diagNeg.remove(r - c)
                diagPos.remove(r + c)
                col.remove(c)
                board[r][c] = "."
            
        
        dfs(0)
        
        return res
