class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        diffMap = [[float("inf")] * COLS for i in range(ROWS)]
        diffMap[0][0] = 0
        visited = [[False] * COLS for i in range(ROWS)]
        heap = [(0, 0, 0)] # diff, r, c
        
        while heap:
            diff, r, c = heapq.heappop(heap)
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited[r][c] = True
            for dr, dc in dirs:
                nxtR = dr + r
                nxtC = dc + c
                
                if 0 <= nxtR < ROWS and 0 <= nxtC < COLS and not visited[nxtR][nxtC]:
                    curDiff = abs(heights[nxtR][nxtC] - heights[r][c])
                    maxDiff = max(curDiff, diffMap[r][c])
                    
                    if diffMap[nxtR][nxtC] > maxDiff:
                        diffMap[nxtR][nxtC] = maxDiff
                        heapq.heappush(heap, (maxDiff, nxtR, nxtC))
            
        return diffMap[-1][-1]
