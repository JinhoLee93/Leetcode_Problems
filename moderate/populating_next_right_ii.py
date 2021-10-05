"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            
            return root
        
        levels = defaultdict(list)
        
        def dfs(root, level):
            if root:
                levels[level].append(root.val)
                
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
                
        dfs(root, 0)
        
        queue = collections.deque([root])
        
        level = 0
        while queue: 
            size = len(queue)
            
            for i in range(size):
                cur = queue.popleft()
                
                if i < size - 1:
                    cur.next = queue[0]
                    
                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
        
        return root
