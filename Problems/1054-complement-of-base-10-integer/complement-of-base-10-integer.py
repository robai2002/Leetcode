class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:return 1
        x = n
        while x>x&(-x):x -= x&(-x)
        return 2*x-n-1
        