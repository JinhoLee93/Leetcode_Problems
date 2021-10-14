class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        pre = [0] * (length + 1)
        
        for l, r, val in updates:
            pre[l] += val
            pre[r + 1] -= val
        
        res, prefix = [], 0
        for i in range(len(pre) - 1):
            prefix += pre[i]
            res.append(prefix)
        
        return res
