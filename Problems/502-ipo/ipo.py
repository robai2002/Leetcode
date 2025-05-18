from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        tasks = sorted(zip(capital, profits), key=lambda x: x[0])
        max_heap = []
        i = 0
        n = len(profits)

        for _ in range(k):
           
            while i < n and tasks[i][0] <= w:
                heapq.heappush(max_heap, -tasks[i][1])
                i += 1
            if max_heap:
                w -= heapq.heappop(max_heap)
            else:
                break
        return w
