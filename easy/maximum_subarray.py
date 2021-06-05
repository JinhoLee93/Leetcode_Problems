# Using Divide and Conquer 
class Solution:
    def conquer(self, nums, index):
        max = conquer(nums, index + 1, l)
        
        if index == len(nums):
            return max
        
    def maxSubArray(self, nums: List[int]) -> int:
        max = -float(inf)
        
        max = conquer(nums, 0, len(nums))
        
        
        
