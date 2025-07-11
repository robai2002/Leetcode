class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[-2 for i in range(n*n)] for j in range(n*n)]

        def solve(x: int,y: int,a: int,b: int) ->int:
            nonlocal n
            #invalid step
            if x<0 or x>=n or y<0 or y>=n or a<0 or a>=n or b<0 or b>=n or grid[a][b] == -1 or grid[x][y] == -1:
               # print(x,y,a,b)
                return -1
            if dp[a*n+b][x*n+y]>-2:
                return dp[a*n+b][x*n+y]
            if a==x and b==y:
                dp[a*n+b][x*n+y] = grid[x][y]
                if a==n-1 and a==b:
                    return dp[a*n+b][x*n+y]
            else:
                dp[a*n+b][x*n+y] =grid[x][y] + grid[a][b]
            
            ans = max(
                solve(x+1,y,a+1,b),solve(x+1,y,a,b+1),solve(x,y+1,a+1,b),solve(x,y+1,a,b+1)
            )
            if ans == -1:
                dp[a*n+b][x*n+y]  = -1
            else:
                dp[a*n+b][x*n+y] += ans
            #print(x,y,a,b,ans,dp[a*n+b][x*n+y])
            return dp[a*n+b][x*n+y]
        
        
        x = solve(0,0,0,0)
        
        return x if x>=0 else 0
             

            