class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = time[:2], time[3:]
        timeList = [char for char in h + m]
        newH, newM = int(h), int(m)
        
        while True:
            strH = ""
            strM = ""
            
            newM += 1
            
            if newM == 60:
                newH += 1
                newM = 0 
            
            if newH == 24:
                newH = 0
            
            if newH < 10: 
                strH += '0'
            strH += str(newH)
            
            if newM < 10:
                strM += '0'
            strM += str(newM)
            
            present = False
            
            newTime = strH + strM
            
            for char in newTime:
                if char in timeList:
                    
                    present = True
                
                else: 
                    
                    present = False
                    break
            
            if present:
                newTime = strH + ':' + strM
                
                return newTime
