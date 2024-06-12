class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        localMaxProfit = 0
        localMin = prices[0]

        for price in prices:
            if price < localMin:
                localMin = price
            localprofit = price - localMin
            if localprofit > localMaxProfit:
                localMaxProfit = localprofit
        return localMaxProfit
        