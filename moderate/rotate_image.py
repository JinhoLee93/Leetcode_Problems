class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Runtime: O(N^2) Memory: O(1)
        visit = set()
        rotate = set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix)): 
                if (r, c) not in visit:
                    temp = matrix[r][c]
                    matrix[r][c] = matrix[(len(matrix) - 1) - c][(len(matrix) - 1) - r]
                    matrix[(len(matrix) - 1) - c][(len(matrix) - 1) - r] = temp

                    visit.add((r, c))
                    visit.add((len(matrix) - 1 - c, len(matrix) - 1 - r))
        
        for i in range(len(matrix)):
            if i not in rotate:
                temp = matrix[i]
                matrix[i] = matrix[len(matrix) - 1 - i]
                matrix[len(matrix) - 1 - i] = temp

                rotate.add(i)
                rotate.add(len(matrix) - 1 - i)
                
