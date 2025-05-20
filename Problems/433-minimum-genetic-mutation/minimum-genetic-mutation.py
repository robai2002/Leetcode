from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Convert bank to a set for O(1) lookup
        lookup = set(bank)
        if endGene not in lookup:
            return -1

        q = deque([(startGene, 0)])

        while q:
            cur, level = q.popleft()
            if cur == endGene:
                return level

            for i in range(len(cur)):
                for c in "ACGT":
                    if cur[i] == c:
                        continue
                    next_str = cur[:i] + c + cur[i+1:]
                    if next_str in lookup:
                        q.append((next_str, level + 1))
                        lookup.remove(next_str)  # Mark as visited

        return -1
