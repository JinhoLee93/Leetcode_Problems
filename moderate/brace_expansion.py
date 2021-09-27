class Solution:
    def expand(self, s: str) -> List[str]:
        expansion = defaultdict(list)
        op = False
        result = []
        visited = set()
        
        i = 0
        for char in s:
            if char == '{':
                op = True
                continue
            
            elif char == '}':
                op = False
                i += 1
                continue
            
            if op:
                if char != ',':
                    expansion[i].append(char)
            
            else:
                expansion[i].append(char)
                i += 1
                
        max_length = len(expansion)
        
        def backtrack(i, res):
            if i == max_length:
                result.append(res)
                return
            
            cur = res 
            for nei in expansion[i]:
                res = cur + nei
                backtrack(i + 1, res)
            
        backtrack(0, "")
        
        return sorted(result)
