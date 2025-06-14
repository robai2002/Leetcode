class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nig = [(1,0),(-1,0),(0,1),(0,-1)]
        n,m = len(matrix),len(matrix[0])
        ans = 0
        dp = [[0 for i in range(m)] for i in range(n)]

        def dfs(i: int,j: int)-> int:

            if dp[i][j]:
                return dp[i][j] 
            for x,y in nig:
                x+=i
                y+=j
                if 0<=x<n and 0<=y<m and matrix[x][y]> matrix[i][j]:
                    dp[i][j] = max(dp[i][j],dfs(x,y))
            dp[i][j] += 1

            return dp[i][j]


        for i in range(n):
            for j in range(m):
                if dp[i][j]==0:
                    ans = max(ans,dfs(i,j))
    
                
        return ans      