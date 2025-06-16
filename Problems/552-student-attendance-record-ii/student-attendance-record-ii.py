class Solution:
    def checkRecord(self, n: int) -> int:
        #a[N][A]
        #l[n][0-2]
        #p[n]
        M = 10**9+7
        dp = [ [[0,0,0],[0,0,0]] for i in range(n+1)]
        dp[0][0][0] =1
        for i in range(n):
       
            for j in range(3):
                dp[i+1][0][0]  = (dp[i][0][j]+dp[i+1][0][0])%M
                dp[i+1][1][0] = (dp[i][0][j]+dp[i][1][j]+dp[i+1][1][0])%M

            for j in range(1,3):
                dp[i+1][0][j] = dp[i][0][j-1]
                dp[i+1][1][j] = dp[i][1][j-1]

        ans = 0
        for i in range(2):
            for j in range(3):
                ans  = (dp[n][i][j]+ans)%M
        return ans
