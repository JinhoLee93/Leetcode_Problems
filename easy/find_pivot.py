class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, partial = sum(nums), 0
        
        for i in range(len(nums)):
            total -= nums[i]
            if total == partial:
                
                return i
        
            partial += nums[i]
            
        return -1
