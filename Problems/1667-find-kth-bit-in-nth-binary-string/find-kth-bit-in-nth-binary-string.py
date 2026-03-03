class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        x = 0
        n = 1<<n
        n -=1
        while n>1:
            # print(n,k)
            if k == (n//2)+1:
                return str(x^1)
            else:
                x^= 1 if k>n//2 else 0
                k = min(k,n-k+1)
            n>>=1
        # print("last")
        return str(x^0)
        