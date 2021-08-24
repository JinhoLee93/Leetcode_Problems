class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prv = self.right, self.left
        
    def remove(self, node): 
        left, right = node.prv, node.nxt
        left.nxt, right.prv = right, left
    
    def insert(self, node): 
        left, right = self.right.prv, self.right
        left.nxt = right.prv = node
        node.prv, node.nxt = left, right
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
                
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
            
        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            self.cache.pop(lru.key)
