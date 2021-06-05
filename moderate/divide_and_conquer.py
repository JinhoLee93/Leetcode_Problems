class Solution:
    def conquer(self, m, nums, index):
        if index == len(nums):
            return m
        
        else:
            if m + nums[index] < nums[index]:
                return self.conquer(nums[index], nums, index + 1) 
            
            # m + nums[index] >= nums[index]
            else:
                return self.conquer(m + nums[index], nums, index + 1)

    def maxSubArray(self, nums: List[int]) -> int:
        m = self.conquer(-float('inf'), nums, 0)
        
        return m
