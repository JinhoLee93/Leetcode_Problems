class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        result = []
        pacificToAtlantic = set()
        atlanticToPacific = set() 
        
        def dfs(r, c, pathmap, prv): 
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in pathmap or \
                heights[r][c] < prv:
                
                return
            
            pathmap.add((r, c))
            dfs(r + 1, c, pathmap, heights[r][c])
            dfs(r - 1, c, pathmap, heights[r][c])
            dfs(r, c + 1, pathmap, heights[r][c])
            dfs(r, c - 1, pathmap, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacificToAtlantic, heights[0][c])
            dfs(ROWS - 1, c, atlanticToPacific, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacificToAtlantic, heights[r][0])
            dfs(r, COLS - 1, atlanticToPacific, heights[r][COLS - 1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) in pacificToAtlantic) and \
                    ((r, c) in atlanticToPacific): 
                    
                    result.append([r, c])
                    
        return result
