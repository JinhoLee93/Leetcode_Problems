class CustomStack:

    def __init__(self, maxSize: int):
        self.increment_dict = defaultdict(lambda:0)
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            
            return -1
        
        tmp = self.increment_dict[len(self.stack) - 1]
        self.increment_dict[len(self.stack) - 2] += tmp
        self.increment_dict[len(self.stack) - 1] = 0
        
        return self.stack.pop() + tmp

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            self.increment_dict[len(self.stack) - 1] += val
        
        else:
            self.increment_dict[k - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
