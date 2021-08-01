class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maximum = float('-inf')
        
        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            
            cur += nums[i]
            maximum = max(maximum, cur)
            
        return maximum
