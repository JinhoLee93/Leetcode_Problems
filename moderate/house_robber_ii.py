class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            
            return nums[0]
        
        return max(self.robbing(nums[:len(nums) - 1]), self.robbing(nums[1:len(nums)]))
    
    def robbing(self, houses):
        money1, money2 = 0, 0
        
        for stack in houses:
            roll = max(stack + money1, money2)
            money1 = money2
            money2 = roll
            
        return money2
