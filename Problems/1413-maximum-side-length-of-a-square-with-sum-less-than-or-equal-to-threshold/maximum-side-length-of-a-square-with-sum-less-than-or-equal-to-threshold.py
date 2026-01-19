class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        n,m = len(mat),len(mat[0])
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = (dp[i][j+1]+dp[i+1][j]-dp[i][j]+mat[i][j])
        
            
        ans,r = 0,max(m,n)
        for i in range(1,n+1):
            for j in range(1,m+1):
                while ans<r and i-ans>0 and j-ans>0:
                    if dp[i][j] - dp[i][j-ans-1] - dp[i-ans-1][j] + dp[i-ans-1][j-ans-1]<=threshold:
                        ans += 1
                    else:
                        break
        return ans