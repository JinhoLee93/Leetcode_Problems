class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        for i in range(len(nums)): 
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            
            else:
                hashmap[nums[i]] = abs(hashmap[nums[i]] - i)
                if hashmap[nums[i]] <= k:
                    return True
                
                else:
                    hashmap[nums[i]] = i
        
        return False
