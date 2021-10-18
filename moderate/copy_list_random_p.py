"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        
        def getClonedNode(node):
            if node:
                if node in visited:
                    
                    return visited[node]
                
                else:
                    visited[node] = Node(node.val, None, None)
                    
                    return visited[node]
                
            return None
        
        if not head:
            
            return head
        
        old = head
        new = Node(old.val, None, None)
        visited[old] = new
        
        while old:
            new.random = getClonedNode(old.random)
            new.next = getClonedNode(old.next)
            
            old = old.next
            new = new.next
        
        return visited[head]
