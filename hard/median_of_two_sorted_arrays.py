class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Using max and min heaps although time: O(N + M)
        small, large = [], []
        nums = nums1 + nums2 
        
        for num in nums:
            heapq.heappush(small, -1 * num)
            
            if (small and large and 
                -1 * small[0] >= large[0]):    
                heapq.heappush(large, -1 * heapq.heappop(small))
            
            if len(small) > len(large) + 1:
                heapq.heappush(large, -1 * heapq.heappop(small))
            
            elif len(small) + 1 < len(large) + 1:
                heapq.heappush(small, -1 * heapq.heappop(large))
            
        if len(small) > len(large):
            
            return -1 * small[0]
        
        elif len(small) < len(large):
            
            return large[0]
        
        return (-1 * small[0] + large[0]) / 2
