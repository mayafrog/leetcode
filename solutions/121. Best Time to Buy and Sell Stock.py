class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum_profit = 0
​
        for i in prices:
            if i < minimum:
                minimum = i
            elif i - minimum > maximum_profit:
                maximum_profit = i - minimum
        
        return maximum_profit
