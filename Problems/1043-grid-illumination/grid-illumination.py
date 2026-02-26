class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        lamp = set()
        
        row = dict()
        col = dict()
        mn_d = dict()
        ax_d = dict()
        
        def remove(i, j):
            row[i] -= 1
            if row[i]==0:del row[i]
            col[j] -= 1
            if col[j]==0:del col[j]
            mn_d[n + i - j] -= 1
            if mn_d[n + i - j] ==0:del mn_d[n + i - j] 
            ax_d[i + j] -= 1
            if ax_d[i + j] ==0:del ax_d[i + j]
        
        # Add lamps (avoid duplicates)
        for x, y in lamps:
            if (x, y) in lamp:
                continue
            lamp.add((x, y))
            if x not in row: row[x]=0
            if y not in col: col[y] =0
            if n+x-y not in mn_d:mn_d[n+x-y] =0
            if x+y not in ax_d: ax_d[x+y]  =0
            row[x] += 1
            col[y] += 1
            mn_d[n + x - y] += 1
            ax_d[x + y] += 1
        
        ans = []
        
        directions = [(0,0),(1,0),(-1,0),(0,1),(0,-1),
                      (1,-1),(1,1),(-1,1),(-1,-1)]
        
        for x, y in queries:
            
            
            if x in row or y in col or n + x - y in mn_d  or x + y in ax_d:
                ans.append(1)
            else:
                ans.append(0)
            
            # Turn off lamps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in lamp:
                    lamp.remove((nx, ny))
                    remove(nx, ny)
        
        return ans