# Runtime: 60 ms, Memory usage: 15.1 MB
# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -float('inf')
        m = max
        
        for i in range(len(nums)):
            if i == 0:
                max = nums[i]
                m = max
                
            else:
                if nums[i] > m + nums[i]:
                    m = nums[i]
                    if m > max:
                        max = m
                else: 
                    m = m + nums[i]
                    if m > max: 
                        max = m
                    
        return max
