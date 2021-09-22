class Solution:
    def reorganizeString(self, s: str) -> str:
        # Use MaxHeap to solve the problem as a greedy algorithm
        counter, heap = Counter(s), []
        res = ""
        
        for key, count in counter.items():
            heapq.heappush(heap, (-1 * count, key))
        
        if -1 * heap[0][0] > (len(s) + 1) // 2:
            
            return ""
        
        while heap:
            first = heapq.heappop(heap)
            res += first[1]
            
            if heap:
                second = heapq.heappop(heap)
                res += second[1]
                
                if first[0] + 1 < 0:
                    heapq.heappush(heap, (first[0] + 1, first[1]))
                
                if second[0] + 1 < 0:
                    heapq.heappush(heap, (second[0] + 1, second[1]))
                    
        return res
