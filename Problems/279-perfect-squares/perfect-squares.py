class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1]*(n+1)
        dp[0] = 0
        def ans(val: int) -> int:
            if dp[val]<=n:
                return dp[val]
            i = 1
            while i*i <= val:
                dp[val] = min(ans(val - i*i) + 1,dp[val])
                i += 1
            return dp[val]

        return ans(n)