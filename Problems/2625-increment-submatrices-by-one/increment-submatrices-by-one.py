class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0 for i in range(n+2)] for i in range(n+2)]

        for x,y,x1,y1 in queries:
            ans[x][y] += 1
            ans[x1+1][y] -=1
            ans[x][y1+1] -= 1
            ans[x1+1][y1+1] += 1

        def get(x: int,y:int)->None:
            if x>0:ans[x][y]+=ans[x-1][y]
            if y>0:ans[x][y] += ans[x][y-1]
            if x>0 and y>0: ans[x][y] -= ans[x-1][y-1]
            return 


        for x in range(n):
            for y in range(n):
                get(x,y)
        return [ans[i][:n] for i in range(n)]