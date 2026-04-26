class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        
        q = []
        grid = [[0]*m for i in range(n)]
        step = [[m+n+2]*m for i in range(n)]
        for x,y,z in sources:
            grid[x][y] = z
            q.append((x,y))
            step[x][y] = 0

        nig = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(n*m):
            x,y = q[i]
            grid[x][y] = abs(grid[x][y])
            for a,b in nig:
                a += x;b+=y
                if 0<=a<n and 0<=b<m and step[a][b]> step[x][y]:
                        grid[a][b] = max(grid[a][b],grid[x][y])
                        if step[a][b]>m+n:
                            q.append((a,b))
                        step[a][b] = step[x][y] + 1
        
        return grid

        