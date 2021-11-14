class Solution:
  def nextPermutation(self, nums):
    N = len(nums)
    
    if N == 1:
      
      return
    
    pivot = 0
    for i in range(N - 1, -1, -1):
      if nums[i] > nums[i - 1]:
        pivot = i
        break
    
    if pivot == 0:
      nums.sort()
      
      return
    
    swap = N - 1
    while nums[swap] <= nums[pivot - 1]:
      swap -= 1
      
    nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
    nums[pivot:] = sorted(nums[pivot:])
    
    return
