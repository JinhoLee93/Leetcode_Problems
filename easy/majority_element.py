class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        res = None
        c = 0 
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
            
            if c < hashmap[nums[i]]:
                c = hashmap[nums[i]]
                res = nums[i]
            
        return res
