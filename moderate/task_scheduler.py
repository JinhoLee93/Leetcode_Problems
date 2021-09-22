class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count, heap = Counter(tasks), []
        res = 0
        
        for key, val in count.items():
            # Always count comes first in the order of heap
            heapq.heappush(heap, (-1 * val, key)) # Be aware of the order of the components of the heaps!!!!!!!!
            
        while heap: 
            restack = []
            cooldown = n
            first = heapq.heappop(heap)
            res += 1
            
            if first[0] + 1 < 0:
                restack.append((first[0] + 1, first[1]))
            
            while cooldown > 0 and len(restack) > 0:
                if heap: 
                    item = heapq.heappop(heap)
                    if item[0] + 1 < 0:
                        restack.append((item[0] + 1, item[1]))
                    
                res += 1
                cooldown -= 1
                
            for i in range(len(restack)):
                heapq.heappush(heap, restack[i])
                
        return res 
