# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        # Do it through two passes
        if not root:
            
            return root
        
        graph = defaultdict(NodeCopy)
        
        def dfs(root):
            if root:
                graph[root] = NodeCopy(root.val)
                
                if root.left:
                    graph[root].left = dfs(root.left)
                    
                if root.right:
                    graph[root].right = dfs(root.right)
                
                return graph[root]
        
        def link(root):
            if root:
                if root.random:
                    graph[root].random = graph[root.random]
                    
                link(root.left)
                link(root.right)
            
        dfs(root)
        link(root) 
        
        return graph[root]
            
