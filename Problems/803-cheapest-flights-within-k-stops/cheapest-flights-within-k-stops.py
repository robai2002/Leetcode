class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # [distance,k,node]
        l = []
        heappush(l,[0,0,src])
        graph = [[] for i in range(n)]
        for x in flights:      
            # destination ,distance
            graph[x[0]].append(x[1:])
        # for l in graph:
        #     print(l)
        dct = {}
        dct[(src,0)] = 0
        while l:
            d,p,node = heappop(l)    
            if node == dst:return d
            if p>k:continue
            if dct[(node,p)] < d:continue
            p += 1
            for q in graph[node]: 
                distance = q[1]+d
                if (q[0],p) not in dct:
                    dct[(q[0],p)] = distance
                    heappush(l,[distance,p,q[0]])
                elif dct[(q[0],p)]>distance:
                    dct[(q[0],p)]= distance
                    heappush(l,[distance,p,q[0]])

        

        return -1

