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
        l = {} 
        
        def randomGen(node): 
            if not node:
                
                return node 
            
            if node in l:
                
                return l[node]
            
            clone = Node(node)
            l[node] = clone
            
            return l[node]
        
        def dfs(node):
            if not node:
                
                return node
            
            clone = Node(node.val)
            l[node] = clone
            l[node].next = dfs(node.next)
            l[node].random = randomGen(node.random)
            
            return l[node]
        
        return dfs(head)
