from typing import List
from functools import cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        def binary_search(ind: int) -> int:
            val = events[ind][1]
            l, r = ind + 1, len(events)

            while l < r:
                mid = (l + r) // 2
                if events[mid][0] > val:
                    r = mid
                else:
                    l = mid + 1

            return l

        @cache
        def solution(ind: int, k: int) -> int:
            if k == 0 or ind >= len(events):
                return 0
           
            res = solution(ind + 1, k)
           
            next_ind = binary_search(ind)
            res = max(res, events[ind][2] + solution(next_ind, k - 1))
            return res

        return solution(0, k)
