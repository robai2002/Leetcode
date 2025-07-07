class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(reverse = True)
        dp = [0 for i in range(n+1)]
        for i in range(n+1):
            if i:
                dp[i] = max(dp[i],dp[i-1])
                while rides and rides[-1][0] == i:
                    s,e,t = rides.pop()
                    dp[e] = max(dp[e],dp[s]+e+t-s)
        
        return dp[n]
            
