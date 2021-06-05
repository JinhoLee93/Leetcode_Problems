# Runtime: 76 ms, Memory usage: 28.9 MB
# O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -float('inf')
        start = 0
        end = len(nums) - 1
        
        for i in range(len(nums)): 
            if max + nums[i] > max:
                start = 0
                end = i
