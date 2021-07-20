class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        minimum = float('inf')
        
        for i in range(len(self.stack)): 
            minimum = min(self.stack[i], minimum)
            
        return minimum
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
