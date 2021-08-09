class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, len(nums)): 
            for j in range(i):
                if i - j > 1:
                    dp[i] = max(dp[i], dp[j] + nums[i])
                    
        return max(dp)
