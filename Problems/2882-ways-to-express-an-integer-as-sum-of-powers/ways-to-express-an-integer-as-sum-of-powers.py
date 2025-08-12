class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        i = 1
        while pow(i,x)<=n:
            d = pow(i,x)
            for j in reversed(range(d,n+1)):
                dp[j] +=dp[j-d] 
            i += 1 
        return dp[-1]%(10**9 +7)