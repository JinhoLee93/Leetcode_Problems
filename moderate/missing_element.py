class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prv, diff = nums[0], 0
        missing = prv + k
        for i in range(1, len(nums)):
            diff = nums[i] - prv - 1
            if 0 < diff <= k:
                missing = prv + diff
                k -= diff 
            
            elif diff > k:
                
                return prv + k
                
            if k == 0:
                
                return missing
            
            prv = nums[i]
            
            if i == len(nums) - 1:
                
                return prv + k
                
        return missing
