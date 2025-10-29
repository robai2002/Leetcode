class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while n>0:
            n//=2
            x*=2
        return x-1
        