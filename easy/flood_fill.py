class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]
        image[sr][sc] = newColor
        pathmap = set() 
        
        def paint(r, c): 
            if r > ROWS - 1 or c > COLS - 1 or \
                r < 0 or c < 0 or \
                (r, c) in pathmap or \
                image[r][c] != originalColor:
                
                return
            
            pathmap.add((r, c))
            
            paint(r + 1, c)
            paint(r - 1, c)
            paint(r, c + 1)
            paint(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == sr + 1 and c == sc) or \
                    (r == sr - 1 and c == sc) or \
                    (r == sr and c == sc + 1) or \
                    (r == sr and c == sc - 1):
                    
                    paint(r, c)
                    
        for (r, c) in pathmap:
            
            image[r][c] = newColor

        return image
      
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        originalColor = image[sr][sc]
        if originalColor == newColor:
            
            return image
        
        def paint(r, c): 
            if image[r][c] == originalColor:
                image[r][c] = newColor

                if r > 0: 
                    paint(r - 1, c)

                if r + 1 < ROWS:
                    paint(r + 1, c)

                if c > 0:
                    paint(r, c - 1)

                if c + 1 < COLS:
                    paint(r, c + 1)
        
        paint(sr, sc)

        return image
