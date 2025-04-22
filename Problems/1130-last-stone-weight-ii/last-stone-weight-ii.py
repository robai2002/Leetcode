class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)//2
        dp = [0]*(s+1)
        dp[0] = 1
        for v in stones:
            for i in reversed(range(v,s+1)):
                if i-v>=0 and dp[i-v]>0:
                    dp[i] = i
        dp[0] = 0
        return (sum(stones)-2*max(dp))
        