# Runtime: 57 ms, Memory Usage: 15 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = buy
        profit = 0
        
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
                sell = buy
            
            if sell < prices[i]:
                sell = prices[i]
            
            profit += (sell - buy)
            buy = sell 
            
        return profit
