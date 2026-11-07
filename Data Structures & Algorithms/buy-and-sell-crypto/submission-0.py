class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profits = []
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):

                # append if there is a profit
                if prices[j] - prices[i] > 0:
                    currProfit = prices[j] - prices[i]
                    profits.append(currProfit)


        if len(profits) != 0:
            maxProfit = max(profits)
        
        return maxProfit