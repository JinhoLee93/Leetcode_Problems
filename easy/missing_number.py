# Faster than 99.9%
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        true_sum = len(nums) * (len(nums) + 1) // 2
        sum_nums = sum(nums)
        
        return true_sum - sum_nums
        
