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
    
        #Brute Force
        class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            
            return []
        
        keypad = {"2": ["a", "b", "c"],
                  "3": ["d", "e", "f"],
                  "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"],
                  "6": ["m", "n", "o"],
                  "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"],
                  "9": ["w", "x", "y", "z"]}
        
        def bruteforce(num, arr, i):
            sub = []
            
            if i == 0:
                for char in keypad[num]: 
                    sub.append(char)
                
            else:
                for char1 in arr:
                    for char2 in keypad[num]:
                        sub.append(char1 + char2)

            return sub
                
        res = []

        for i in range(len(digits)):
            if digits[i] not in keypad:
                
                return []
            
            res = bruteforce(digits[i], res, i)
            
        return res
