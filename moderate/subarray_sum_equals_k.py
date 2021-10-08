class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        indicies = defaultdict()
        
        for idx, val in enumerate(nums):
            indicies[idx] = val + indicies.get(idx - 1, 0)
            
        for i in range(len(indicies)):
            if indicies[i] == k:
                count += 1
            
            for j in range(i): 
                if indicies[i] - indicies[j] == k:
                    count += 1
            
        return count
