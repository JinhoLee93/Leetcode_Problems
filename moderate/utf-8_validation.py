class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        numBytes = 0
        for i in range(len(data)): 
            datum = str(format(data[i], "08b"))
            if numBytes == 0:
                for bit in datum:
                    if bit == '0':
                        break
                    numBytes += 1
                    
                if numBytes == 0:
                    continue

                if numBytes == 1 or numBytes > 4:
                    
                    return False
                
            
            else:
                if datum[:2] != "10":
                    
                    return False
                
            numBytes -= 1
        
        return numBytes == 0

