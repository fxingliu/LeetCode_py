class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        ret, valley = 0, prices[0]
        for p in prices:
            ret = max(ret, p-valley)
            valley = min(valley, p)
        return ret
