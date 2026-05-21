class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        l = list(int(c) for c in s)
        return False if any(True for x,y in pairwise(l) if abs(x-y)>2) else True 
        