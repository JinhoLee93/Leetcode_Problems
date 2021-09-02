class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time: O(R * C * Number of Rotten Oranges), Space: O(R * C)
        ROWS, COLS = len(grid), len(grid[0])
        pathSet = set()
        count = 2
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c): 
            nonlocal count 
            
            pathSet.add((r, c))
            for direction in directions:
                nxtRow, nxtCol = r + direction[0], c + direction[1]
                rRange, cRange = 0 <= nxtRow < ROWS, 0 <= nxtCol < COLS
                if rRange and cRange and grid[nxtRow][nxtCol] == 1 and (nxtRow, nxtCol) not in pathSet:
                    grid[nxtRow][nxtCol] = count + 1

        while True:
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == count and (r, c) not in pathSet:
                        dfs(r, c)
            
            if len(pathSet) > 0:
                count += 1
                pathSet.clear()
            
            else:
                break
                
        for r in range(ROWS):
            if 1 in grid[r]:
                
                return -1
        
        finalCount = count - 3
        
        return finalCount if finalCount > 0 else 0
