class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m ,ans = len(grid),len(grid[0]), 0
        x = [[0 for i in range(m)] for j in range(n)]
        y = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':x[i][j] += 1
                if grid[i][j] == 'Y':y[i][j] += 1
                if i>0:
                    x[i][j] += x[i-1][j]
                    y[i][j] += y[i-1][j]
                if j>0:
                    x[i][j] += x[i][j-1]
                    y[i][j] += y[i][j-1]
                if j>0 and j>0:
                    x[i][j] -= x[i-1][j-1]
                    y[i][j] -= y[i-1][j-1]
                if x[i][j]>0 and x[i][j] == y[i][j]:
                    ans += 1
        return ans