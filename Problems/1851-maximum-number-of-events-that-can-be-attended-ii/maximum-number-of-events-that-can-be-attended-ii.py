class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        n = len(events)
        events.sort(key =lambda x:x[1])
        dp = [[0 for i in range(k+1)]for i in range(n+1)]
        ends = [ event[1] for event in events ]

        for i in range(n):
            s,e,v = events[i]
            ind = bisect.bisect_right(ends,s-1)
            for j in range(1,k+1):
                dp[i+1][j] = max(dp[i][j],v+dp[ind][j-1])
        

        return dp[-1][-1]
      
