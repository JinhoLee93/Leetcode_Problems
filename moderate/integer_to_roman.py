# Runtime: 45 ms, Memory usage: 14.1 MB (less than 95%)

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        num = str(num)
        res = ""
        
        for i in range(len(num)):
            n = int(num[i]) * (10 ** ((len(num) - 1) - i))
            
            if n in roman:
                res += roman[n] 
            
            else:
                if n > 0 and n < 9:
                    part = ""
                    while n > 0:
                        if n in roman:
                            part += roman[n]
                            n -= n
                        
                        else:
                            part += roman[1]
                            n -= 1
                            
                    
                    res += part[::-1]
                
                elif n > 10 and n < 100:
                    part = ""
                    while n > 0:
                        if n in roman:
                            part += roman[n]
                            n -= n
                        
                        else:
                            part += roman[10]
                            n -= 10
                    
                    res += part[::-1]
                
                elif n > 100 and n < 1000:
                    part = ""
                    while n > 0:
                        if n in roman:
                            part += roman[n]
                            n -= n
                        
                        else:
                            part += roman[100]
                            n -= 100
                    
                    res += part[::-1]
                
                elif n > 1000:
                    part = ""
                    while n > 0:
                        if n in roman:
                            part += roman[n]
                            n -= n
                            
                        else:
                            part += roman[1000]
                            n -= 1000
                        
                    res += part[::-1]
                    
        return res
