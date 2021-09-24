# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        queue = collections.deque([(root, 0)])
        
        while queue: 
            root, col = queue.popleft()
            
            if root: 
                columns[col].append(root.val)
                
                queue.append((root.left, col - 1))
                queue.append((root.right, col + 1))
                
        return [columns[key] for key in sorted(columns.keys())]
