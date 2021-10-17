class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            
            return 0
        
        cost, heap = [], []
        
        for stick in sticks:
            heapq.heappush(heap, stick)
            
        while heap:
            cur_sum = heapq.heappop(heap)
            
            if not heap:
                break
            
            else:
                cur_sum += heapq.heappop(heap)
                heapq.heappush(heap, cur_sum)
                cost.append(cur_sum)
        
        return sum(cost)
