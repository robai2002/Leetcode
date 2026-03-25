class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(x for row in grid for x in row)
        if s&1: return False
        n, m = len(grid), len(grid[0])
        x = 0

        for i in range(n):
            if x*2==s:return True
            for j in range(m):
                x += grid[i][j]
        for j in range(m):
            if x*2==s:return True
            for i in range(n):
                x-= grid[i][j]

        return False
        