class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l = k//2
        for j in range(y,y+k):
            for i in range(l):
                grid[x+i][j],grid[x+k-1-i][j] = grid[x+k-1-i][j],grid[x+i][j]
        return grid
                