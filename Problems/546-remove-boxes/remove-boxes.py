from functools import cache
from itertools import groupby
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @cache
        def dfs(grps: tuple) -> int:
            if not grps:
                return 0
            (colorL, lenL), grps = grps[0], grps[1:]

            res = lenL * lenL + dfs(grps)

            for i, (colorR, lenR) in enumerate(grps):
                if colorL == colorR:
                    merged = ((colorL, lenL + lenR),) + grps[i + 1:]
                    res = max(res, dfs(grps[:i]) + dfs(merged))

            return res

        box_grps = tuple((k, len(list(g))) for k, g in groupby(boxes))
        return dfs(box_grps)
