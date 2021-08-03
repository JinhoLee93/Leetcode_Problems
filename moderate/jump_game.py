class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = 0
        
        for i in range(len(nums) - 1):
            if nums[i] > max_step:
                max_step = nums[i]
            
            max_step -= 1
            if max_step < 0:

                return False
            
        return True
