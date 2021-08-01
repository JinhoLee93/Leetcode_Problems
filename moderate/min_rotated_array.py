# Runtime: 24 ms (faster than 99.9%), Memory usage: 14.4 MB
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        
        while i < j: 
            if nums[i + 1] < nums[i]:
                
                return nums[i + 1]
            
            else:
                i += 1
            
            if nums[j - 1] > nums[j]:
                
                return nums[j]
            
            else:
                j -= 1
        
        return nums[0]
