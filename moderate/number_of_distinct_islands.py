class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Time: O(M*N) Space: O(M*N) (since pathSet is the biggest)
        ROWS, COLS = len(grid), len(grid[0])
        pathSet = set()
        uniqueSet = set()
        
        def dfs(r, c, direction):
            if r < 0 or c < 0 or \
                r > ROWS - 1 or c > COLS - 1 or \
                (r, c) in pathSet or \
                grid[r][c] != 1:
                
                return 
            
            pathSet.add((r, c))
            directions.append(direction)
            
            dfs(r + 1, c, "D")
            dfs(r - 1, c, "U")
            dfs(r, c + 1, "R")
            dfs(r, c - 1, "L")
            
            directions.append("O")
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in pathSet and grid[r][c] == 1:
                    directions = []
                    dfs(r, c, "O")
                    
                    if directions:
                        uniqueSet.add(tuple(directions))
            
        return len(uniqueSet)
