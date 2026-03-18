class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        cnt = 0
        n,m = len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if i>0:grid[i][j] += grid[i-1][j]
                if j>0:grid[i][j] += grid[i][j-1]
                if i>0 and j>0:grid[i][j]-=grid[i-1][j-1]
                if grid[i][j]<=k:cnt+= 1
        return cnt
        