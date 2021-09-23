class Solution:
    # Right Solution 
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if max(milestones) > sum(milestones) - max(milestones):
            
            return (sum(milestones) - max(milestones)) * 2 + 1
        
        else:
            
            return sum(milestones)
        
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
