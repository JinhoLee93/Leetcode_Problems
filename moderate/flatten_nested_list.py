# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque(nestedList)
        self.iter = collections.deque([])
        while self.queue:
            cur = self.queue.popleft()
            if cur.getInteger() != None:
                self.iter.append(cur.getInteger())
        
            else:
                if cur.getList():
                    for i in range(len(cur.getList()) - 1, -1, -1):
                        self.queue.appendleft(cur.getList()[i])

    def next(self) -> int:
        
        return self.iter.popleft()
    
    def hasNext(self) -> bool:
        
        return len(self.iter)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
