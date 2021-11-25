class Solution:
    def compress(self, chars: List[str]):
        s = ""
        counter = i = 0
        
        while True:
            if i > len(chars) - 1:
                if 1 < c < 10:
                    chars.insert(i, str(c))
                
                elif c > 9:
                    num = str(c)
                    for n in num:
                        chars.insert(i, n)
                        i += 1

                break
                
            if chars[i] != s:
                if s != "":
                    if 1 < c < 10:
                        chars.insert(i, str(c))
                        i += 1
                    
                    elif c > 9:
                        num = str(c)
                        for n in num:
                            chars.insert(i, n)
                            i += 1
                        
                s = chars[i]
                i += 1
                c = 1
                
                continue
            
            chars.pop(i)
            c += 1
            
        
        return len(chars)
