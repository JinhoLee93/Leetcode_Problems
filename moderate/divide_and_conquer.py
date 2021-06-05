class Solution:
    def conquer(self, m, nums, index):
        if index == len(nums):
            return m
        
        else:
            if 
            if m + nums[index] < nums[index]:
                return self.conquer(nums[index], nums, index + 1) 
            
            elif m + nums[index] >:
                return self.conquer(m + nums[index], nums, index + 1)

    def maxSubArray(self, nums: List[int]) -> int:
        m = self.conquer(-float('inf'), nums, 0)
        
        return m
