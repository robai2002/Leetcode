class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return True
            parent[pa] = pb
            return False

        for i in range(m):
            for j in range(n):
                idx = i * n + j

                if i > 0 and grid[i][j] == grid[i-1][j]:
                    if union(idx, (i-1)*n + j):
                        return True

                if j > 0 and grid[i][j] == grid[i][j-1]:
                    if union(idx, i*n + j-1):
                        return True

        return False