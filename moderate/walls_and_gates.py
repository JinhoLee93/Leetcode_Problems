class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Time: O(4 * R * C), Space = O(1)
        ROWS, COLS = len(rooms), len(rooms[0])
        emptyRoom = 2147483647
        pathSet = set() 
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # !!Check the cells ahead of the door!!
        def dfs(r, c, prv):
            nonlocal directions, rooms
            
            for direction in directions:
                nxtRow, nxtCol = r + direction[0], c + direction[1]
                rRange, cRange = 0 <= nxtRow < ROWS, 0 <= nxtCol < COLS
                
                if rRange and cRange and rooms[nxtRow][nxtCol] != -1 and rooms[nxtRow][nxtCol] > prv:
                    rooms[nxtRow][nxtCol] = prv
                    dfs(nxtRow, nxtCol, prv + 1)
            
            return prv
            
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    dfs(r, c, 1)
