class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Time: O(NlogN), Space: O(N)
        timeInt = []
        diff = float("inf")
        
        for time in timePoints:
            timeInt.append(int(time[:2]) * 60 + int(time[3:]))

        timeInt.sort()
        
        for i in range(len(timeInt) - 1):
            diff = min(diff, timeInt[i + 1] - timeInt[i])
            if diff == 0:
                
                return diff
        
        diff = min(diff, abs(timeInt[-1] - (timeInt[0] + (24 * 60)))) 
            
        return diff
