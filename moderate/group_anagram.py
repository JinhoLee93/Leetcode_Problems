class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for ana in strs:
            anagrams["".join(sorted(ana))].append(ana)
        
        return [val for val in anagrams.values()]
