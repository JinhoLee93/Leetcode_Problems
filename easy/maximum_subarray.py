# Using Divide and Conquer 
class Solution:
    def conquer(self, m, nums, index):
        if index == len(nums):
            return m
        
        else:
            if m + nums[index] < nums[index]:
                
                return self.conquer(nums[index], nums, index + 1) 
            
            else:
                
                return self.conquer(m + nums[index], nums, index + 1)
        
    def maxSubArray(self, nums: List[int]) -> int:
        m = -float('inf')
        m = self.conquer(m, nums, 0)
        
        return m
