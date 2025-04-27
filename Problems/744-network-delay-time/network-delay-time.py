class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [10**5 for i in range(n+1)]
        graph = [[] for i in range(n+1)]
        for (x,y,z) in times:
            graph[x].append([z,y])
        
        def dijkstra(start):
            pq = [(0,start)]
            time[start] = 0
            while pq:
                cur_time ,cur_node = heapq.heappop(pq)
                if cur_time>time[cur_node]:
                    continue

                for t,adj  in graph[cur_node]:
                    if t + cur_time < time[adj]:
                        time[adj] = t + cur_time
                        heapq.heappush(pq,(t+cur_time,adj))
            x = max(time[1:])
            return x if x<10**5 else -1
        return dijkstra(k)