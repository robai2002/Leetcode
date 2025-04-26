class Solution:
    def totalCost(self, cost: List[int], k: int, candidates: int) -> int:
        l,r =0,-1
        h = []
        n = len(cost)
        ans = 0
        while k:
            if l<candidates and l-r<= n:
                heappush(h,[cost[l],l])
                l += 1
            elif -r<=candidates and l-r<= n:
                heappush(h,[cost[r],n+r])
                r -= 1
            else:
                a,b = heappop(h)
                ans += a
                k -= 1
                if l-r<=n and b<l:
                    heappush(h,[cost[l],l])
                    l += 1
                elif l-r<=n :
                    heappush(h,[cost[r],n+r])
                    r -= 1

        return ans
                