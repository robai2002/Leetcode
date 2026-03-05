class Solution:
    def minOperations(self, s: str) -> int:
        x,a,b = 48,0,0
        for ch in s:
            if ord(ch) == x:
                b += 1
            else:
                a += 1
            x ^= 1
        return min(a,b)