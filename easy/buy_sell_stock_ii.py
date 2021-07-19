# Runtime: 60 ms, Memory Usage: 15 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        win1 = 0
        profit = 0
        
        for i in range(len(prices)): 
            if win1 < i:
                if prices[i] > prices[win1]:
                    profit += prices[i] - prices[win1]
                
                win1 += 1
            
        return profit
