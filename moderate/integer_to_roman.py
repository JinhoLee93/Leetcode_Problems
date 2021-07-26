class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        num = str(num)
        res = ""
        
        for i in range(len(num)):
            n = int(num[i]) * (10 ** ((len(num) - 1) - i))
            
            if n in roman:
                res += roman[n] 
            
            else:
                if n != 0 and n + (10 ** ((len(num) - 1) - i)) in roman:
                    res += roman[10 ** ((len(num) - 1) - i)]
                    res += roman[n + (10 ** ((len(num) - 1) - i))]
                
                if n < 4:
                    j = 0
                    while j < n:
                        res += roman[1]
                        j += 1
                
                if n > 5 and n < 9:
                    
                    
                        
                if n > 10 and n < 40:
                    j = 0
                    while j < n:
                        res += roman[10]
                        j += 10
                
                if n > 50 and n < 90:
                    
                
                if n > 100 and n < 400:
                    
                if n > 500 and n < 900:
                    
        return res
