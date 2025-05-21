class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p = [0]*n
        m = 1e5
        for i,v in enumerate(prices):
            m = min(m,v)
            if i:
                p[i] = p[i-1]
            p[i] = max(v-m,p[i])
        m = 0
        ans = 0
        for i in range(n-1,-1,-1):
            m = max(m,prices[i])
            p[i] += m-prices[i]
        return max(p)