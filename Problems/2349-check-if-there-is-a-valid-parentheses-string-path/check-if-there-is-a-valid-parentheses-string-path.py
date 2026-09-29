class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])

        length = n + m -1
        if length&1:
            return False
        
        @cache
        def solve(i: int, j: int, val: int)->bool:
            if i==n or j==m:return False
            val += 1 if grid[i][j]=='(' else -1
            if val<0 or val>n-i + m-j -2:
                return False
            if i == n-1 and j==m-1:
                return val==0
            return solve(i+1,j,val) or solve(i,j+1,val)



        return solve(0,0,0)