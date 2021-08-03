class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= i:
                return True
            
        return False
