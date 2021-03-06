class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Array Manipulation
        nums = sorted([(v, i) for i, v in enumerate(nums)])
        
        i, j = 0, 1
        
        while j < len(nums):
            if nums[i][0] == nums[j][0]:
                if abs(nums[i][1] - nums[j][1]) <= k:
                    
                    return True
                
                else:
                    i += 1
                    j = i + 1

            else:
                i += 1
                j = i + 1
                
        return False
    
        # Hash
        numTable = {}
        
        for idx, num in enumerate(nums):
            if num not in numTable:
                numTable[num] = idx
            
            else:
                if abs(numTable[num] - idx) <= k:
                    
                    return True
                
                else:
                    numTable[num] = idx
                
        return False
        
        
        
