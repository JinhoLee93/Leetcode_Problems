class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        remain = defaultdict(int)
        
        for t in time:
            t %= 60
            if t == 0:
                res += remain.get(0, 0)
            
            else:
                res += remain.get(60 - t, 0)
                
            remain[t] += 1

        return res
