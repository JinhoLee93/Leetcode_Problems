class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = max(nums)
        cur_max, cur_min = 1, 1
        
        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
                continue
            
            temp = n * curmax
            curmax = max(n * cur_max, n * cur_min, n)
            curmin = min(temp, n * cur_min, n)
            maximum = max(maximum, cur_max)
        
        return maximum
