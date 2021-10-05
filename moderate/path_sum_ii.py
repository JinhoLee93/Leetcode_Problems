# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathList = []
        
        def backtrack(root, total, pathNodes, pathList):
            if not root:
                
                return 
            
            pathNodes.append(root.val)
            
            if total == root.val and not root.left and not root.right:
                pathList.append(list(pathNodes))
            
            else:
                backtrack(root.left, total - root.val, pathNodes, pathList)
                backtrack(root.right, total - root.val, pathNodes, pathList)
                
            pathNodes.pop()
        
        backtrack(root, targetSum, [], pathList)
        
        return pathList
