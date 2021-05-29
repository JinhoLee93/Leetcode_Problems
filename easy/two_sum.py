class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Big O should be < O(n^2)
        for i in range(len(nums)):
            t = target - nums[i]
            
            if t in nums and i != nums.index(t):
                return [i, nums.index(t)]
