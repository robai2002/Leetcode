class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = 1 - n&1
        while n:
            if x==n&1:
                return False
            x ^= 1
            n>>=1
        return True
        