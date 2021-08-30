class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        s = set(nodes)
        res = None
        
        def dfs(node):
            nonlocal res
            if not node:
                
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node in s
            
            if left + right + mid >= 2:
                res = node
                
            return left or right or mid
        
        dfs(root)
        
        return res if res else nodes[0]
