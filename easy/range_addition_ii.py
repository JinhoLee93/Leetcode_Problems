class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r_min, c_min = float("inf"), float("inf")
        
        for row, col in ops:
            if row < r_min: 
                r_min = row
            
            if col < c_min:
                c_min = col
                
        return r_min * c_min if ops else m * n
