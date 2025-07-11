class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        @cache
        def solve(r1, c1, r2, c2):
            if not (0<=r1<N and 0<=c1<N and 0<=r2<N and 0<=c2<N): return -inf
            if not (grid[r1][c1]!=-1 and grid[r2][c2]!=-1): return -inf
            if r1>r2: return solve(r2, c2, r1, c1) # speed up
            if r1==c1==r2==c2==N-1: return grid[N-1][N-1]
            cp = grid[r1][c1] + (grid[r2][c2] if r1!=r2 or c1!=c2 else 0)
            f1 = solve(r1+1, c1, r2+1, c2)
            f2 = solve(r1+1, c1, r2, c2+1)
            f3 = solve(r1, c1+1, r2+1, c2)
            f4 = solve(r1, c1+1, r2, c2+1)
            return cp + max(f1, f2, f3, f4)
        return max(solve(0, 0, 0, 0), 0)