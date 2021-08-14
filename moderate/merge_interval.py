class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn), O(N)
        intervals = sorted(intervals, key= lambda i:i[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                
                merged[-1] = [min(merged[-1][0], intervals[i][0]), max(merged[-1][1], intervals[i][1])]
            
            elif merged[-1][1] < intervals[i][0]:
                
                merged.append(intervals[i])
            
            
        return merged
