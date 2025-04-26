class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        
        queue = deque()
        seen = set()
        seen_route = set()
        queue.append(source)
        seen.add(source)
        ans = 0


        while queue:
            n = len(queue)
            print(queue,ans)
            while n:
                n -=1
                stop = queue.popleft()
    
                if stop == target:
                    return ans
                for ind in graph[stop]:
                    if ind in seen_route: continue
                    seen_route.add(ind)
                    
                    for stop in routes[ind]:
                        if stop not in seen:
                            queue.append(stop)
                            seen.add(stop)
            ans += 1



        return -1