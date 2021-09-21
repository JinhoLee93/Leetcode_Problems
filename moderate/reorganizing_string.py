class Solution:
    def reorganizeString(self, s: str) -> str:
        counter, hp = Counter(list(s)), []
        
        for key in counter:
            heapq.heappush(hp, ((-1) * counter[key], key))
            
        item = hp[0]
        
        if item[0] * (-1) > (len(s) + 1) // 2: 
            
            return ''
        
        result = []
        
        while hp:
            item = heapq.heappop(hp)
            result.append(item[1])
            if hp:
                item2 = heapq.heappop(hp)
                result.append(item2[1])
                if item[0] + 1 < 0: 
                    heapq.heappush(hp, (item[0] + 1, item[1]))
                    
                if item2[0] + 1 < 0: 
                    heapq.heappush(hp, (item2[0] + 1, item2[1]))
                    
        return ''.join(result)
