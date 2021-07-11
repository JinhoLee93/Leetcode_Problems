# Runtime: 28 ms, Memory usage: 14.2 MB
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = list()
        
        tri.append([1])
        
        for i in range(rowIndex + 1):
            if i != 0:
                sub = list()
                sub.append(1)
                for j in range(len(tri[i - 1]) - 1):
                    sub.append(tri[i - 1][j] + tri[i - 1][j + 1])
                
                sub.append(1) 
                
                tri.append(sub)
                
        return tri[rowIndex]
