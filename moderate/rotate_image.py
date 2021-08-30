class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time: O(N) Space: O(N) N being the number of cells
        ROWS = COLS = len(matrix)
        length = len(matrix) - 1
        rotateSet = set() 
        reflectSet = set()
        
        # Rotation 
        for r in range(ROWS):
            for c in range(COLS): 
                if (r, c) not in rotateSet: 
                    temp = matrix[r][c]
                    matrix[r][c] = matrix[length - c][length - r]
                    matrix[length - c][length - r] = temp
                    
                    rotateSet.add((r, c))
                    rotateSet.add((length - c, length - r))
        
        # Transpose
        for i in range(ROWS):
            if not i in reflectSet:
                temp = matrix[i]
                matrix[i] = matrix[length - i]
                matrix[length - i] = temp 
                
                reflectSet.add(i)
                reflectSet.add(length - i)
