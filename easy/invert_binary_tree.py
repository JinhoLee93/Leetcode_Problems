# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
            
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    # BFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            
            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
                
        return root
