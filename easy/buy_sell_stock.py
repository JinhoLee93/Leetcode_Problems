# Faster than 95% and less memory usage than 55%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = buy
        net = 0

        for i in range(len(prices)): 
            if buy > prices[i]:
                buy = prices[i]
                sell = buy
            
            if sell < prices[i]:
                sell = prices[i]
                if (sell - buy) > net:
                    net = sell - buy
        
        return net
