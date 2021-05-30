# I could've solved this problem with little or no effort with list comprehension, yet I wanted to practice trie data tree.
class Node:
    def __init__(self, children, isShared, count):
        self.children = children
        self.isShared = isShared
        self.count = count

class Solution:
    def __init__(self):
        self.trie = None
        
    def build(self, words):
        self.trie = Node({}, False, 0)
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node({}, False, 1)
                else:
                    current.children[char].isShared = True
                    current.children[char].count += 1
                    
                current = current.children[char]
        
    def buildPrefix(self, words, prefix):
        for word in words:
            pre = ""
            current = self.trie
            for char in word: 
                if current.children:
                    if current.children[char].count == len(words):
                        pre += char
                current = current.children[char]
                        
            prefix.append(pre)
            
        return prefix
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        self.build(strs)
        prefix = []
        self.buildPrefix(strs, prefix)
        
        if len(prefix) == 0 or "" in prefix:
            return ""
        else:
            return prefix[-1]
