class Solution:
  def permute(self, nums):
    res = []
    
    def backtrack(i):
      if i == len(nums):
        res.append(nums[:])
        
        return
      
      visited = set()
      
      for j in range(i, len(nums)):
        if nums[j] not in visited:
          nums[i], nums[j] = nums[j], nums[i]
          backtrack(i + 1)
          nums[i], nums[j] = nums[j], nums[i]
          visited.add(nums[i])
      
      backtrack(0)
      
      return res
