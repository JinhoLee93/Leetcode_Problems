# Runtime: 44 ms, Memory usage: 14.9 MB
# Only allowed to implement a function with O(n log n) runtime complexity
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        else:
            nums.append(target)
            nums = sorted(nums)
            
            return nums.index(target)
        
