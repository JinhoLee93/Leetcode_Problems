class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = []
        minimum = None
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                minimum = target - (nums[i] + nums[j] + nums[k])
                
                if minimum > target:
                    k -= 1
                
                elif minumum < target:
                    j += 1
                
                else: 
                    
            
