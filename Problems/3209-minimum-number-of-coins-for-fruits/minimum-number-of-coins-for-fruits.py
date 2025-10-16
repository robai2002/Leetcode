class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(idx = 0)-> int:
            if idx >= n: return 0
            return prices[idx]+ min(dp(i) for i in range(idx+1, 2*idx+3))
        

        n = len(prices)
        return dp()