class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islandSet = set()
        numOfIsland = 0
        
        def dfs(r, c, i):
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in islandSet or \
                grid[r][c] != 1:
                
                return
            
            islandSet.add((r, c))
            dfs(r + 1, c, i)
            dfs(r - 1, c, i)
            dfs(r, c + 1, i)
            dfs(r, c - 1, i)
            
        i = 0
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    if (r, c) not in islandSet:
                        dfs(r, c)
                        i += 1
        
        return numOfIsland 
