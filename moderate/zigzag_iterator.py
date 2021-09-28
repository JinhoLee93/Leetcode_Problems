class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.iter = collections.deque([])
        self.v1, self.v2 = collections.deque(v1), collections.deque(v2)
        
        while self.v1 and self.v2:
            self.iter.append(self.v1.popleft())
            self.iter.append(self.v2.popleft())
            
        if self.v1:
            while self.v1:
                self.iter.append(self.v1.popleft())
        
        elif self.v2:
            while self.v2:
                self.iter.append(self.v2.popleft())
        
    def next(self) -> int:
        
        return self.iter.popleft()

    def hasNext(self) -> bool:
        
        return len(self.iter)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
