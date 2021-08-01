class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        res = nums[0]
        
        def divide_and_conquer(cur, res, i):
            if i == len(nums):
                return res
            
            if cur < 0: 
                cur = 0
            
            cur += nums[i]    
            res = max(res, cur)
            
            return divide_and_conquer(cur, res, i + 1)
        
        res = divide_and_conquer(cur, res, 0)
            
        return res
