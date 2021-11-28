class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def union(s: str) -> List[tuple]:
            uni = []
            count = 1
            char = ""
            
            for i in range(len(s)):
                if char != s[i]:
                    if char == "":
                        char = s[i]
                        continue
                    
                    else:
                        uni.append((char, count))
                        char = s[i]
                        count = 1
                
                else:
                    count += 1
            
            uni.append((char, count))
                
            return uni
        
        def check(sSub: List[tuple], wSub: List[tuple]) -> bool:
            if len(sSub) != len(wSub):
                
                return False 
            
            for i in range(len(sSub)):
                if sSub[i][0] != wSub[i][0] or (sSub[i][1] < 3 and sSub[i][1] != wSub[i][1]) or \
                    sSub[i][1] < wSub[i][1]:
                    
                    return False
                
            return True
        
        sSub = union(s)
        res = 0
        
        for word in words:
            wSub = union(word)
            
            if check(sSub, wSub):
                res += 1

        return res
