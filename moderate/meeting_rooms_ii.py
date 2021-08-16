class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time: O(NlogN), Space: O(N)
        start, end = [], []
        numOfRooms, count = 0, 0
        startP, endP = 0, 0
        
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        
        start.sort()
        end.sort()
            
        while startP < len(start) and endP < len(end):
            if min(start[startP], end[endP]) == start[startP]:
                if start[startP] == end[endP]:
                    count -= 1
                    endP += 1
                
                else:
                    count += 1
                    startP += 1
            
            else:
                count -= 1
                endP += 1
            
            numOfRooms = max(numOfRooms, count)
            
        return numOfRooms
