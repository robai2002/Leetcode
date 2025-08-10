class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = set()
        x = 1
        for _ in range(31):
            s.add(tuple(sorted(str(x))))
            x *= 2
        
        return tuple(sorted(str(n))) in s
