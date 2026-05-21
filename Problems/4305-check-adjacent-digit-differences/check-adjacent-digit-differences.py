class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        digits = map(int, s)
        return all(abs(a - b) <= 2 for a, b in pairwise(digits))