import heapq
from collections import defaultdict
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for f,t,p in flights:
            graph[f].append((p,t))

        dist = [float('inf') for i in range(n)]
        dist[src] = 0

        queue = deque()
        queue.append((0, src, 0)) 
     


        while queue:

            stops,source,price = queue.popleft()
            if stops>k:
                continue
          

            for p,v in graph[source]:

                alt = price+p

                if alt<dist[v] :
                    
                    dist[v] = alt
                    queue.append((stops+1,v,alt))
        out =  dist[dst]

        return out if out!=float('inf') else -1





        


        