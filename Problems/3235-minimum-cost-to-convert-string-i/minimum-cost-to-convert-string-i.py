import string
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str], cost: List[int]) -> int:

        inf = 10**13
        mp = {}

        # direct transformations
        for o, ch, cst in zip(original, changed, cost):
            mp[o + ch] = min(mp.get(o + ch, inf), cst)

        # self cost
        for ch in string.ascii_lowercase:
            mp[ch + ch] = 0

        # Floyd–Warshall on characters
        for k in string.ascii_lowercase:
            for i in string.ascii_lowercase:
                for j in string.ascii_lowercase:
                    mp[i + j] = min(
                        mp.get(i + j, inf),
                        mp.get(i + k, inf) + mp.get(k + j, inf)
                    )

        ans = 0
        for ch, ch1 in zip(source, target):
            if ch != ch1:
                if mp.get(ch + ch1, inf) >= inf:
                    return -1
                ans += mp[ch + ch1]

        return ans
