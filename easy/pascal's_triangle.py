# Runtime: 28 ms, Memory usage: 14.3 MB
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = list()
        
        for i in range(numRows): 
            if i == 0:
                tri.append([1])
                
            else:
                sub = list()
                sub.append(1)
                
                for j in range(len(tri[i - 1]) - 1):
                    sub.append(tri[i - 1][j] + tri[i - 1][j + 1])
                        
                sub.append(1)
                tri.append(sub)
        
        return tri
