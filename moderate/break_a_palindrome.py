class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        res = ""
        
        if len(palindrome) == 1:
            
            return res
        
        letters = defaultdict(int)
        for idx, letter in enumerate(string.ascii_lowercase):
            letters[letter] = idx

        length = len(palindrome)
        a = [False] * int(length)
        
        if length % 2 == 0:
            for i in range(length):
                if i == 0 and palindrome[i] == 'a':
                    res += palindrome[i]
                    a[i] = True
                    
                if 0 < i < length - 1 and a[i - 1] == True and palindrome[i] == 'a':
                    res += palindrome[i]
                    a[i] = True
                
                if palindrome[i] != 'a':
                    res += 'a'
                    
                    return res + palindrome[i + 1:length]
                
                if i == (length - 1) and a[i - 1] and palindrome[i] == 'a':
                    res += 'b'
            
            return res
        
        else:
            for i in range(length):
                if i == 0 and palindrome[i] == 'a':
                    res += palindrome[i]
                    a[i] = True
                    
                if 0 < i < length - 1 and a[i - 1] == True and palindrome[i] == 'a':
                    res += palindrome[i]
                    a[i] = True
                
                if palindrome[i] != 'a':
                    tmp = res + 'a' + palindrome[i + 1:length]
                    if tmp == tmp[::-1]:
                        res += palindrome[i]
                        a[i] = True
                        continue
                    
                    else:
                        
                        return tmp
                
                if i == (length - 1) and a[i - 1] and palindrome[i] == 'a':
                    res += 'b'
                
            return res
