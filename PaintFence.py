class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0, k, k*k]
        for i in range(3, n+1):
            dp.append((k-1)*(dp[i-2]+dp[i-1]))
        return dp[n]
