class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        def a(val,i,j): grid[i][j] = val; return (val,i,j)
        if  grid[0][0] or grid[-1][-1]:   return 0
        
        n,d = len(grid), [(-1,0),(0,1),(1,0),(0,-1)]
        q   = deque((1,i,j) for i,j in product(range(n),range(n)) if grid[i][j])
        while q:
            step,i,j = q.popleft()
            q.extend(a(step+1,i+di,j+dj) for (di,dj) in d if 0<=i+di<n and 0<=j+dj<n and not grid[i+di][j+dj])

        sq = SortedList([(grid[0][0],0,0)])
        while sq:
            dist,i,j = sq.pop()
            if  (i==n-1 and j==n-1) or (dist==1): return dist-1
            for (di,dj) in d:
                if 0<=i+di<n and 0<=j+dj<n and grid[i+di][j+dj]:
                    sq.add((min(dist, grid[i+di][j+dj]),i+di,j+dj))
                    grid[i+di][j+dj] = 0
        return  -1
        