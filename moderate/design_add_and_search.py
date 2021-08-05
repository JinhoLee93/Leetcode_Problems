class TrieNode:
    
    def __init__(self): 
        self.children = {}
        self.is_last_chr = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]
            
        cur.is_last_chr = True
            

    def search(self, word: str) -> bool:
        cur = self.trie
        
        def dfs(root, j):
            cur = root
            
            for i in range(j, len(word)):
                char = word[i]
                
                if char == ".":
                    for child in cur.children.values():
                        if dfs(child, i + 1): 
                            
                            return True 
                        
                    return False
                
                else:
                    if char not in cur.children:
                        
                        return False
                    
                    cur = cur.children[char]
            
            return cur.is_last_chr
        
        return dfs(cur, 0)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
