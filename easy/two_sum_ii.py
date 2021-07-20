class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        
        for i, j in enumerate(numbers): 
            if j in d:
                return d[j], i + 1
            
            d[target-j] = i + 1
