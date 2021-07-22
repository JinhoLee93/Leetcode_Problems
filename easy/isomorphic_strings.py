class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap.keys() and t[i] not in hashmap.values():
                hashmap[s[i]] = t[i]
            
            elif s[i] not in hashmap.keys() and t[i] in hashmap.values():
                return False
            
            if  hashmap[s[i]] != t[i]:
                return False
            
        return True
