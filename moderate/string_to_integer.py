class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0 
        
        if not str.isdigit(s[0]):
            if s[0] == '+' or s[0] == '-':
                pass
            elif s[0] == ' ':
                pass
            else:
                return 0
        
        res = ""
        
        for i in range(len(s)): 
            if s[i] != ' ': 
                if len(res) == 0:
                    if s[i] == '+' or s[i] == '-':
                        res += s[i]
                        
                    if s[i] == '0':
                        if i < len(s) - 1:
                            if not str.isdigit(s[i + 1]):
                                return 0
                            
                    if str.isalpha(s[i]):
                        break
                        
                else:
                    if not str.isdigit(s[i]):
                        break

                if str.isdigit(s[i]): 
                    if s[i] == '0':
                        if len(res) > 0:
                            res += s[i]
                    else:
                        res += s[i]
            
            else:
                if len(res) > 0:
                    break
        
        if len(res) == 0:
            return 0
            
        if len(res) == 1 and (res[0] == '+' or res[0] == '-'):
            return 0
        
        if int(res) >= (-2) ** 31 and int(res) <= (2 ** 31) - 1: 
            return int(res)
        
        if int(res) < (-2) ** 31:
            return (-2) ** 31
        
        if int(res) > (2 ** 31) - 1:
            return (2 ** 31) - 1 
