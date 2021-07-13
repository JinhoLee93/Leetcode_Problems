class Node:
    def __init__(self, val=None, child=None, count=0): 
        val = val
        child = child 
        count = count

class trie:
    def __init__(self):
        head = None
    
    def build(self, string): 
        self.head = Node()
        
        for letter in string: 
            
    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 
        
        
        tri = trie()
        tri.build(s)
        
        
        
        
