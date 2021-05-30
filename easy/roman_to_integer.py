class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = [str(i) for i in str(s)]
        switch = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        for i in range(len(roman) - 1):
            if switch[roman[i]] < switch[roman[i + 1]]:
                if switch[roman[i]] == 1:
                    res -= 1
                
                if switch[roman[i]] == 10:
                    res -= 10
                
                if switch[roman[i]] == 100:
                    res -= 100
