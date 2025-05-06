class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for i in range(n)]

        for (s,d),p in zip(edges,succProb):
            graph[s].append((d,p))
            graph[d].append((s,p))

        queue  = []
        probability = [0.0 for i in range(n)]
        probability[start_node] = -1.0
        heapq.heappush(queue,(probability[start_node],start_node))
        
        while queue:
            
            prob,node = heapq.heappop(queue)

            if node == end_node:
                return -prob

            if probability[node] < prob:continue

            for x,p in graph[node]:

                if probability[x] >p*prob:
                    probability[x] = p*prob
                    heapq.heappush(queue,(probability[x],x))

        return 0
            
            
