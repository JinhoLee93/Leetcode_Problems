class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Time: timsort < heapsort < quicksort < mergesort
        
        res = []
        heapq.heapify(nums)
        
        while nums:
            res.append(heapq.heappop(nums))
            
        return res
