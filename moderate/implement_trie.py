class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_last_chr = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
            
        cur.is_last_chr = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        
        for c in word:
            if c not in cur.children:
                
                return False
            
            cur = cur.children[c]
            
        
        return cur.is_last_chr
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        
        for c in prefix:
            if c not in cur.children:
                
                return False
            
            cur = cur.children[c]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
