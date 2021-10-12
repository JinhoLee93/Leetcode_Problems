class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        cur_max = 0
        
        for i in range(len(nums)): 
            if nums[i] == 1:
                cur_max += 1
                
            else:
                cur_max = 0
                if maximum >= len(nums) - i - 1:
                    break
            
            maximum = max(maximum, cur_max)
            
        return maximum
