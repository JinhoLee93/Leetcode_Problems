class Solution:
    def findKthLargest(self, nums, k):
        # Heap
        
        return heapq.nlargest(k, nums)[-1]
      
        # Sorting
        
        return sorted(nums, key=reverse)[k - 1]
      
        # Quick Select
        
        return 
