class Solution:
    def minimumFlips(self, n: int) -> int:
        ans = 0
        z = n
        while n:
            ans<<=1
            ans+=n%2
            n>>=1
        return bin(ans^z).count("1")