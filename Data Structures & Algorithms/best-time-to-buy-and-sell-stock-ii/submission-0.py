class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)): # starting from 2nd element beacuse for every i with check the value with the previous index's value so, skipping the first value i.e at 0th index
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
        
        