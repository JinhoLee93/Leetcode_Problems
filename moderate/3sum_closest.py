class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('inf')
        mindis = float('inf')
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                three = nums[i] + nums[j] + nums[k]
                dis = abs(target - three) 
                if mindis > dis: 
                    mindis = dis
                    res = three
                
                if three > target:
                    k -= 1
                elif three < target:
                    j += 1
                else:
                    return nums[i] + nums[j] + nums[k]
                
        return res
