class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):

            # check to see if you can make a better profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)

            else:
                # if you find a new lowest point, make this the new left
                left = right
            right += 1

        return maxP