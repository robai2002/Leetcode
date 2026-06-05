class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(reverse = True)
        N = max(f[0] for f in items)
        dp = [0 for i in range(N+10)]
        m = {}
        for x,y in items:
            m[x] = m.get(x,0)+1
        ff = m.keys() 
        for x in ff:
            dp[x] = m[x]
            for i in range(x*2,N+2,x):
                if m.get(i,0)>0:
                    dp[x] += m[i]
        
        b = [0 for i in range(budget+1)]
        p = min(f[1] for f in items)
        for x,y in items:
            if dp[x]==1:continue
            a = dp[x]
            for i in range(budget,y-1,-1):
                b[i] = max(b[i],b[i-y]+a)
                #print(i,b[i],i,y,i-y,b[i-y],a)
           # print(x,y,b)
        return max(b[i]+ (budget-i)//p for i in range(budget+1))