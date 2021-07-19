class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numset = list()
        for i in range(len(nums)):
            if nums[i] not in numset:
                numset.append(nums[i])
            
            else:
                numset.remove(nums[i])

                
        return numset[0]
