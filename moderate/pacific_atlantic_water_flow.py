class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time: O(N * M + N + M) = O(N * M)
        # Space: O(N + M)
        ROWS, COLS = len(heights), len(heights[0])
        pacificToAtlantic = set()
        atlanticToPacific = set()
        
        res = []
        
        def dfs(r, c, prvHeight, pathmap):
            if r < 0 or c < 0 or \
                r > (ROWS - 1) or c > (COLS - 1) or \
                (r, c) in pathmap or \
                heights[r][c] < prvHeight:
                
                return
            
            pathmap.add((r, c))
            
            dfs(r + 1, c, heights[r][c], pathmap)
            dfs(r - 1, c, heights[r][c], pathmap)
            dfs(r, c + 1, heights[r][c], pathmap)
            dfs(r, c - 1, heights[r][c], pathmap)
            
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacificToAtlantic)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlanticToPacific)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacificToAtlantic)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlanticToPacific)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificToAtlantic and \
                    (r, c) in atlanticToPacific:
                    
                    res.append([r, c])
                    
        return res
