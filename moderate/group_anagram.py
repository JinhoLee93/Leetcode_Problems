class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for anagram in strs:
            og = anagram
            anagram = list(anagram)
            anagram.sort()
            anagram = "".join(anagram)
            
            if not res:
                res[anagram].append(og)
                continue
            
            if anagram in res:
                res[anagram].append(og)
                
            else:
                res[anagram].append(og)
                
        return [val for val in res.values()]
