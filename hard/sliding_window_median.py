class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Simple Sorting
        window = 0
        medians = []
        
        for i in range(k - 1, len(nums)):
            med = sorted(nums[window:window + k])
            median = 0
            # k is an even number
            if k % 2 == 0:
                median = (med[k // 2] + med[(k // 2) - 1]) / 2
                
            # k is an odd number
            else: 
                median = med[k // 2]
                
            medians.append(median)    
            window += 1
        
        return medians
        
        # Heap Removal (Time Exceeded)
        window = 0
        medians = [] 
        
        for i in range(k - 1, len(nums)):
            median = self.findMedian(nums[window:window + k])
            
            medians.append(median)
            window += 1
        
        return medians
    
    def findMedian(self, arr):
        maxHeap, minHeap = [], []
        
        for i in range(len(arr)): 
            heapq.heappush(maxHeap, -1 * arr[i])
            
            if (maxHeap and minHeap) and -1 * maxHeap[0] > minHeap[0]:
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
            
            if len(maxHeap) + 1 < len(minHeap):
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap))
            
            elif len(maxHeap) > len(minHeap) + 1:
                heapq.heappush(minHeap, -1 * heapq.heappop(maxHeap))
        
        if len(maxHeap) > len(minHeap):
            
            return -1 * maxHeap[0]
        
        elif len(maxHeap) < len(minHeap):
            
            return minHeap[0]
        
        else:
            return (-1 * maxHeap[0] + minHeap[0]) / 2
