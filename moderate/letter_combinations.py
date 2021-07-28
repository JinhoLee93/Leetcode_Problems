class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return None
        
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        
        def backtrack(i, cur_str):
            if len(cur_str) != len(digits):
                for c in hashmap[digits[i]]:
                    backtrack(i + 1, cur_str + c)
            
            else:
                res.append(cur_str)
                
        backtrack(0, "")
                
        return res
