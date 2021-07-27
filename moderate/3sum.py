class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return None
        
        else:
            nums = sorted(nums)
            l1 = []
            
            for i in range(len(nums)):
                j, k = i + 1, len(nums) - 1
                
                while j < k:
                    three_sum = nums[i] + nums[j] + nums[k]
                    
                    if three_sum > 0:
                        k -= 1
                    
                    elif three_sum < 0:
                        j += 1
                        
                    else:
                        if [nums[i], nums[j], nums[k]] not in l1:
                            l1.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
            
            return l1
