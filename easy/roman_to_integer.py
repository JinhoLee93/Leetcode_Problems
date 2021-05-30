class Solution:
    def romanToInt(self, s: str) -> int:
        # Turns the given Roman number into an integer 
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
        
        for i in range(len(roman)):
            if i < len(roman) - 1:
                # Edge cases
                if switch[roman[i]] < switch[roman[i + 1]]:
                    if switch[roman[i]] == 1:
                        res -= 2

                    if switch[roman[i]] == 10:
                        res -= 20

                    if switch[roman[i]] == 100:
                        res -= 200
            
            res += switch[roman[i]]
        
        return res
