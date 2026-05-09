class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        ans = [[0]*m for i in range(n)]
        def C(xx: int,yy: int,zz: int) ->List[int]:
            if xx<yy:return [0,xx]
            elif xx<yy+zz-1: return [xx-yy+1,yy-1]
            elif xx< 2*yy+zz-2: return [zz-1,2*yy+zz-3-xx]
            else: return [2*(zz+yy-2)-xx,0]
        z = 2*(m+n-2)
        for j in range(min(n,m)//2):
            for i in range(z):
                a,b = C(i,m-2*j,n-2*j)
                a+=j
                b+=j
                f = (i+k)%z
                c,d = C(f,m-2*j,n-2*j)
                c+= j
                d += j
                ans[a][b] = grid[c][d]
           
            z-=8
        return ans