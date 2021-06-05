# Runtime: 76 ms, Memory usage: 28.9 MB
class Solution:
    def conquer(self, m, res, nums, index):
        if index == len(nums):
            return res
        
        else:
            if m + nums[index] < nums[index]:
                if nums[index] > res:
                    res = nums[index]
                    
                return self.conquer(nums[index], res, nums, index + 1) 
            
            else: 
                if m + nums[index] > res:
                    res = m + nums[index]
                
                return self.conquer(m + nums[index], res, nums, index + 1)

    def maxSubArray(self, nums: List[int]) -> int:
        res = self.conquer(-float('inf'), -float('inf'), nums, 0)
        
        return res
