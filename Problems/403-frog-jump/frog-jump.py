from functools import cache
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        m = {stone: i for i, stone in enumerate(stones)}
        
        @cache
        def solve(ind: int, k: int) -> bool:
            if ind == len(stones) - 1:
                return True

            for step in [k-1, k, k+1]:
                if step > 0:
                    next_pos = stones[ind] + step
                    if next_pos in m:
                        if solve(m[next_pos], step):
                            return True
            return False
        return solve(0, 0)
