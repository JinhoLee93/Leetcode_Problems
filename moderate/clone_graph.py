"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node 
        
        clones = {} 
        clones[node] = Node(node.val)
        q = collections.deque()
        q.append(node)
        
        while q: 
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                clones[cur].neighbors.append(clones[neighbor])
            

        return clones[node]

# DFS
