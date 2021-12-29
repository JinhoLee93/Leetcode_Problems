class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            
            return []
        
        res = []
        phone = {'2': "abc",
                 '3': "def",
                 '4': "ghi",
                 '5': "jkl",
                 '6': "mno",
                 '7': "pqrs",
                 '8': "tuv",
                 '9': "wxyz"}
        
        def backtrack(tmp, i):
            if i == len(digits):
                res.append(tmp)
                
                return
            
            for char in phone[digits[i]]:
                backtrack(tmp + char, i + 1)
            
        backtrack("", 0)
            
        return res
        
