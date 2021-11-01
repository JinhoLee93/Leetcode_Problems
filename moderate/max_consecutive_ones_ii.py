
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum, l, r, zerolen = 0, 0, 0, 0
        
        while r < len(nums):
            if nums[r] == 0:
                zerolen += 1
            
            while zerolen == 2:
                if nums[l] == 0:
                    zerolen -= 1
                l += 1
                
            maximum = max(maximum, r - l + 1)
            r += 1

        return maximum
