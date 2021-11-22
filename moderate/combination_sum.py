class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(i, sub, target):
            if target == 0:
                res.append(sub.copy())
                
                return
            
            elif target < 0:
                
                return
            
            for j in range(i, len(candidates)):
                sub.append(candidates[j])
                backtrack(j, sub, target - candidates[j])
                sub.pop()
        
        backtrack(0, [], target)
        
        return res
                
