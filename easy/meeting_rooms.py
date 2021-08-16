class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time: O(NlogN), Space: O(N)
        intervals = sorted(intervals, key=lambda i: i[0])
        
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                
                return False
            
        return True
