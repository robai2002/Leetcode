import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        cnt = [0 for i in range(n)]
        used = []

        for start,end in meetings:
            while used and used[0][0] <=start:
                _,room = heapq.heappop(used)
                heapq.heappush(free,room)

            if not free:
                _,room = heapq.heappop(used)
                end += _-start
                heapq.heappush(free,room)
            
            room = heapq.heappop(free)
            cnt[room] += 1
            heapq.heappush(used,(end,room))
        
        return cnt.index(max(cnt))