class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(v, i) for i, v in enumerate(nums)])
        
        i = 0
        j = 1
        
        while j < len(nums):
            if abs(nums[i][0] - nums[j][0]) <= t:
                if abs(nums[i][1] - nums[j][1]) <= k:
                    return True
                else:
                    j += 1
            
            else:
                i += 1
                j = i + 1
        
        return False
