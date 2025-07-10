class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp =[[n,n,n] for i in range(n+1)]
        dp[0][1] = 0
        y = -1
        for i,a in enumerate(obstacles,start = 1):
            a -= 1
            for j in range(3):
                if j==a or j == y:
                    dp[i][j] = n
                elif a>=0 :
                    dp[i][j] = min(dp[i-1][j],dp[i-1][a]+1)
                else:
                    dp[i][j] = dp[i-1][j]
            y = a
    
        return min(dp[-1]) 