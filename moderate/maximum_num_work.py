class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # Right Solution, Space: O(1), Time: O(N)
        maximum, summation = max(milestones), sum(milestones)
        
        return (summation - maximum) * 2 + 1 if maximum > summation - maximum else summation
        
    # Heap Solution (Limited Time Exceeded)
    def numberOfWeeks(self, milestones: List[int]) -> int:
        works = {idx: val for idx, val in enumerate(milestones)}
        heap, res = [], 0
        
        for key, val in works.items():
            heapq.heappush(heap, (-val, key))
            
        while heap:
            first = heapq.heappop(heap) 
            
            res += 1
            
            if heap:
                second = heapq.heappop(heap)
                
                if first[0] + 1 < 0:
                    heapq.heappush(heap, (first[0] + 1, first[1]))
                
                if second[0] + 1 < 0:
                    heapq.heappush(heap, (second[0] + 1, second[1]))
                    
                res += 1
        
        return res
