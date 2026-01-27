class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[]for i in range(n)]
        for u,v,w in edges:
            graph[u].append([v,w])
            graph[v].append([u,w*2])
        cost = [10**9 for i in range(n)]
        
        cost[0] = 0
        q = []
        heappush(q,[0,0])
        while q:
            x,y = heappop(q)
            
            if cost[y]<x:
                continue
            if y==n-1:
                return x 
            for a,b in graph[y]:
                #print(a,b,x,cost[a])
                if x+b<cost[a]:
                    cost[a] = x+b
                    heappush(q,[x+b,a])
            #print(y)
            #print(cost)

        return -1
                    