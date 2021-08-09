class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            
            return nums[0]
    
        dp1 = nums[:len(nums) - 1]
        dp2 = nums[1:len(nums)]
    
        for i in range(len(dp1)):
            for j in range(i):
                if i - j > 1: 
                    dp1[i] = max(dp1[i], nums[i] + dp1[j])
                
        for i in range(len(dp2)):
            for j in range(i):
                if i - j > 1:
                    dp2[i] = max(dp2[i], nums[i + 1] + dp2[j])
                
        
        d1 = max(dp1)
        d2 = max(dp2)
        
        return max(d1, d2)
                
