class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Time: O(N), Space: O(N)
        dp = {0: 0}
        maxLength, tmp_sum = 0, 0
        
        for idx, num in enumerate(nums):
            tmp_sum += num
            
            if tmp_sum - k in dp:
                maxLength = max(maxLength, (idx + 1) - dp[tmp_sum - k])
                
            if tmp_sum not in dp:
                dp[tmp_sum] = idx + 1
                    
        return maxLength
