class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(N), Space: O(N)
        intervals.sort(key = lambda i:i[0])
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            mergepoint = merged[-1][1]
            
            if mergepoint >= start:
                merged[-1][1] = max(mergepoint, end)
            
            else:
                merged.append([start, end])
            
        return merged
