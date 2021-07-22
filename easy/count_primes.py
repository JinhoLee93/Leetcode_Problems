class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True] * n
        
        i = 2
        while i * i < len(primes):
            if primes[i]:
                j = i
                while i * j < len(primes):
                    primes[i * j] = False
                    j += 1
            
            i += 1
        
        # - index 0, 1
        return primes.count(True) - 2
