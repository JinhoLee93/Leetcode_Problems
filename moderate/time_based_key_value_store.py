class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashTable:
            self.hashTable[key] = []

        self.hashTable[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashTable:
            
            return ""
            
        if timestamp < self.hashTable[key][0][1]:
            
            return ""
        
        elif timestamp > self.hashTable[key][-1][1]:
            
            return self.hashTable[key][-1][0]
        
        # Binary Search to find the exact timestamp
        l, r = 0, len(self.hashTable[key]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if self.hashTable[key][mid][1] == timestamp:
                
                return self.hashTable[key][mid][0]
            
            if self.hashTable[key][mid][1] < timestamp:
                l = mid + 1
                
            else:
                r = mid - 1
        
        return self.hashTable[key][r][0]
    
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
