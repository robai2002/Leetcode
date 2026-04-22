class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dis = [[distanceThreshold+3]*n for i in range(n)]

        for u,v,w in edges:
            dis[u][v] = min(dis[u][v],w)
            dis[v][u] = min(dis[v][u],w)
        
        for i in range(n):
            dis[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        mx = n
        ans = -1
        print(dis)
        for i in range(n):
            x = sum(1 for j in range(n) if dis[i][j]<=distanceThreshold and i!= j)
            if x<=mx:
                mx = x
                ans = i
        
        return ans