class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(N+M), Space: O(N+M)
        ROWS, COLS = len(grid), len(grid[0])
        pathSet = set()
        maxArea = 0
        
        def dfs(r, c):
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in pathSet or \
                grid[r][c] != 1:
                
                return 
            
            pathSet.add((r, c))
            curIsland.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(ROWS):
            for c in range(COLS):  
                if grid[r][c] == 1:
                    if (r, c) not in pathSet:
                        curIsland = set()
                        dfs(r, c)
                        maxArea = max(maxArea, len(curIsland))
                        
        return maxArea
