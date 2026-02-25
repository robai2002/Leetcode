class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones)-1)%(k-1):
            return -1
        arr = [0] 
        for ind,stone in enumerate(stones):
            arr.append(arr[ind]+stone)
        

        @cache
        def solve(x: int,y: int,s: int) -> int:
            
            if x>=y:return 0
            cost = 10**10
            for i in range(x,y,s):
                cost = min(cost,solve(x,i,s)+solve(i+1,y,s))
            if (y-x)%s==0:
                cost += arr[y+1]-arr[x]
            return cost

        return solve(0,len(stones)-1,k-1) 
        