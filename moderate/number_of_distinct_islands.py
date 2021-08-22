class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Time: O(M+N) Space: O(M+N)
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        uniqueIslands = set()
        
        def dfs(r, c, direction):
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in seen or \
                grid[r][c] != 1:
                
                return
            
            seen.add((r, c))
            curIsland.append(direction)
            dfs(r + 1, c, 'D')
            dfs(r - 1, c, 'U')
            dfs(r, c + 1, 'R')
            dfs(r, c - 1, 'L')
            curIsland.append('O')
            
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    if (r, c) not in seen:
                        curIsland = []
                        dfs(r, c, 'O')
                        if curIsland:
                            uniqueIslands.add(tuple(curIsland))
        
        return len(uniqueIslands)
