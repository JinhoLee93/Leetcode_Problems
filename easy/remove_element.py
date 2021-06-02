# runtime: 24 ms, Memory usage: 13.9 MB
# Only allowed to implement O(1) extra memory
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums): 
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
