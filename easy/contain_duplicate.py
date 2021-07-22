class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        
        for i in range(len(nums)): 
            if nums[i] not in res:
                res.add(nums[i])
            else:
                return True        
            
            
        return False
