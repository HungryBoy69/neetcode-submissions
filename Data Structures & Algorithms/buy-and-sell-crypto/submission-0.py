class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we need to keep track of the min price and each day subtract the current price with the minimum price
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price 
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        return  max_profit
        
            