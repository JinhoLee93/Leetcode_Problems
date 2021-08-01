class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) % 2 == 0:
            l, r = (len(nums) // 2) - 1, len(nums) // 2
        
        else:
            l, r = len(nums) // 2, len(nums) // 2
            
        while l > -1 and r < len(nums):
            if nums[l] == target:
                return l
            
            if nums[r] == target:
                return r
            
            l -= 1
            r += 1
            
                
        return -1
