class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)] # diff, r, c
        grid[0][0] = -1
        
        while heap:
            val, r, c = heapq.heappop(heap)
            
            if r == ROWS - 1 and c == COLS - 1:
                
                return -val
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dirR, dirC in dirs:
                nxtR = dirR + r
                nxtC = dirC + c
                
                if 0 <= nxtR < ROWS and 0 <= nxtC < COLS and 0 <= grid[nxtR][nxtC]:
                    minVal = min(-val, grid[nxtR][nxtC])
                    heapq.heappush(heap, (-minVal, nxtR, nxtC))
                    grid[nxtR][nxtC] = -1
