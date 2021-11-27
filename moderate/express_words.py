class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def group_words(word: str) -> list[tuple]:
            group = []
            i = 0
            while i < len(word):
                char = word[i]
                start = i
                while i < len(word) and word[i] == char:
                    i += 1
                group.append((char, i-start))

            return group
        
        def check_stretchy(s_group: list[tuple], word_group: list[tuple]) -> bool:
            if len(s_group) != len(word_group):
                
                return False
            
            for i in range(len(s_group)):
                if s_group[i][0] != word_group[i][0] or s_group[i][1] < word_group[i][1] or (s_group[i][1] > word_group[i][1] and s_group[i][1] < 3):
                    
                    return False
                
            return True
        
        ans = 0
        s_group = group_words(s)
        
        for word in words:
            word_group = group_words(word)
            if check_stretchy(s_group, word_group):
                ans += 1
                
        return ans
