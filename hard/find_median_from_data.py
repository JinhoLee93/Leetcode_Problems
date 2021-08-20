class MedianFinder:
    # Time: O(logN) Space: O(N)
    def __init__(self):
        """
        initialize your data structure here.
        """
        # small = Max Heap
        # large = Min Heap
        self.small, self.large = [], []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        # When max value (small = max heap) is bigger than min value (large = min heap)
        if (self.small and self.large and (-1 * self.small[0]) >= self.large[0]):
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))
            
        # When length is out of the tune (len + 1)
        if len(self.small) > (len(self.large) + 1):
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))
            
        elif len(self.large) > (len(self.small) + 1):
            heapq.heappush(self.small, (-1 * heapq.heappop(self.large)))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            
            return self.large[0]
        
        elif len(self.small) > len(self.large):
            
            return (-1 * self.small[0])
        
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
