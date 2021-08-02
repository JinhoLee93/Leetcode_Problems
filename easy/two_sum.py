class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashmap: 
                hashmap[nums[i]] = i
            
            if (target - nums[i]) in hashmap:
                if hashmap[target - nums[i]] != i:
                    return [hashmap[target - nums[i]], i]
