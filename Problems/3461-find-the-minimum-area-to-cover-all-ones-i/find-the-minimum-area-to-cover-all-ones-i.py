class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x,y,a,b=-1,-1,-1,-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if a<0:
                        a = i
                    if x<0:
                        x = j
                    else:
                        x = min(x,j)
                    b,y = max(b,i),max(y,j)

        return (b-a+1)*(y-x+1) if y>=0 else 0 

        