class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        
        n = len(h)
        m = len(h[0])
        l = []
        mx = SortedList()
        for i in range(n):
            heapq.heappush(l,[h[i][0],i,0])
            heapq.heappush(l,[h[i][m-1],i,m-1])
            mx.add(h[i][0])
            mx.add(h[i][-1])
            h[i][0] = h[i][m-1] = -1

        for i in range(1,m-1):
            heapq.heappush(l,[h[0][i],0,i])
            heapq.heappush(l,[h[n-1][i],n-1,i])
            mx.add(h[0][i])
            mx.add(h[-1][i])
            h[0][i] = h[-1][i] = -1
        # l.sort()
        
        nig = [(-1,0),(1,0),(0,1),(0,-1)]
        
        ans = 0
        val = mx[0]
        print(val)
        while l:
            a,b,c = heapq.heappop(l)
            
            val = max(val,mx[0])
           # print(a,b,c,val,end = " ")
            #print(val)
            mx.remove(a)
            for x,y in nig:
                x += b
                y += c
                if 0<=x<n and 0<=y<m and h[x][y]>=0:
                    ans += max(0, val - h[x][y])
                    heapq.heappush(l,[h[x][y],x,y])
                    mx.add(h[x][y])
                    h[x][y] = -1
           # print(ans)
            #print(a,b,c,ans)
        return ans
       




            
