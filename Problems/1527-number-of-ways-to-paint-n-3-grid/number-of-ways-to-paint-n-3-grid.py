class Solution:
    def numOfWays(self, n: int) -> int:
        same,diff,mod =6,6,10**9+7
        for i in range(n-1):same,diff = (3*same+2*diff)%mod , 2*(same+diff)%mod
        return (same+diff)%mod