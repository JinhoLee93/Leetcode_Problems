class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(i, sub, target):
            if target == 0:
                res.append(sub.copy())
                
                return
            
            elif target < 0:
                
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    
                    continue
                
                if candidates[j] > target:
                    
                    return
                
                sub.append(candidates[j])
                backtrack(j + 1, sub, target - candidates[j])
                sub.pop()
                
        
        backtrack(0, [], target)
        
        return res
