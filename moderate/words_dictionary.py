class TrieNode:
    
    def __init__(self): 
        self.children = {}

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
            

    def search(self, word: str) -> bool:
        for c in word:
            if c == '.':
                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
