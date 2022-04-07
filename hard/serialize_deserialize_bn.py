# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = "" 
        
        def dfs(root): 
            nonlocal res
            
            if not root: 
                res += "None,"
                
            else:
                res += str(root.val) + ","
                dfs(root.left)
                dfs(root.right)
                
        dfs(root)
        
        return res
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(",")
        res.pop()
        
        def dfs(res):
            if res[0] == "None":
                
                res.pop(0)
                return
            
            node = TreeNode(res[0])
            res.pop(0)
            
            node.left = dfs(res)
            node.right = dfs(res)
            
            return node
            
        
        return dfs(res)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
