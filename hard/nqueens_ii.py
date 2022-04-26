class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        leftToRight, rightToLeft, col = set(), set(), set() 
        
        def dfs(r): 
            nonlocal res
            
            if r == n:
                res += 1
                
                return
            
            for c in range(n):
                if (r - c) in leftToRight or (r + c) in rightToLeft or c in col:
                    continue 
                    
                leftToRight.add(r - c)
                rightToLeft.add(r + c)
                col.add(c)
                
                dfs(r + 1)
            
                leftToRight.remove(r - c)
                rightToLeft.remove(r + c)
                col.remove(c)
                
        dfs(0)
        return res
    
