class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = n
        x = str(x)[::-1]
        x = int(x)
        return abs(n-x)
        