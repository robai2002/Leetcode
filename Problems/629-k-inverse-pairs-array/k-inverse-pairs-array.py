class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0:
            return 1
        dp = [[0 for i in range(k+1)] for i in range(n+1)]
        for i in range(k+1):dp[0][i] = 1
        mod = 10**9+7
        for i in range(1,n):
            for j in range(k+1):
                dp[i][j] = dp[i-1][j]
                dp[i][j] -= 0 if j-i-1<0 else dp[i-1][j-i-1]
                dp[i][j]=(dp[i][j] + mod)%mod
                if j>0:
                    dp[i][j]=(dp[i][j] + dp[i][j-1])%mod                  
       # print(dp)
      
        return (mod+dp[n-1][k] - dp[n-1][k-1])%mod

        