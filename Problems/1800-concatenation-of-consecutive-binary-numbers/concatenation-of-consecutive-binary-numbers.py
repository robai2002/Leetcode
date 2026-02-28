class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans,mod = 0,10**9+7

        for i in range(1,n+1):
            s = len(bin(i))-2
            ans<<=s
            ans = (ans+i)%mod
        return ans
            
        