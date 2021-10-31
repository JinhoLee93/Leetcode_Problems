class Solution:
  def permute(self, nums):
    res = []
    
    def backtrack(i):
      if i == len(nums):
        res.append(nums[:])
       
      for j in range(i, len(nums):
        nums[i], nums[j] = nums[j], nums[i]
        backtrack(i + 1)
        nums[i], nums[j] = nums[i], nums[j]
                     
    backtrack(0)
    
    return res
