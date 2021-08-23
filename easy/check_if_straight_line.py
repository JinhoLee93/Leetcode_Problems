class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            
            return True 
        
        for i in range(len(coordinates) - 2):
            x1, y1 = coordinates[i][0], coordinates[i][1]
            x2, y2 = coordinates[i + 1][0], coordinates[i + 1][1]
            x3, y3 = coordinates[i + 2][0], coordinates[i + 2][1]
            
            area = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if area != 0:
                
                return False
            
        return True
