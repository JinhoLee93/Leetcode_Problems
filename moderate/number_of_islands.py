class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islandCount = 0
        pathmap = set()

        def dfs(r, c):
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in pathmap or \
                grid[r][c] != "1":
                
                return
        
            pathmap.add((r, c))
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in pathmap:
                    dfs(r, c)
                    islandCount += 1

        return islandCount
