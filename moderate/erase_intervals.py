class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(NlogN), Space: O(N)
        intervals = sorted(intervals, key=lambda i:i[1])
        newIntervals = [intervals[0]]
        count = 0
        
        for i in range(1, len(intervals)):
            if newIntervals[-1][1] <= intervals[i][0]:
                newIntervals.append(intervals[i])
                
            else:
                count += 1
                
        return count
