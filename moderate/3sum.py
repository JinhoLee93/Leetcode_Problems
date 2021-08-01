class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        three = 0
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                three = nums[i] + nums[j] + nums[k]
                
                if three > 0:
                    k -= 1
                
                elif three < 0:
                    j += 1
                
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res
