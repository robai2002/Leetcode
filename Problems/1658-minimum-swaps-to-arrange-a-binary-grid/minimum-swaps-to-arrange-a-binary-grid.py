class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr = []
        n = len(grid)
        for l in grid:
            i = n-1
            while i>=0 and l[i]==0:i-=1
            arr.append(n-i-1)
        ans = 0
        # print(arr)
        for i in range(n):
            x = i
            while x<n and arr[x]<n-i-1:x+= 1
            
            if x==n:return -1
            for ind in range(x,i,-1):
                ans += 1
                arr[ind],arr[ind-1] = arr[ind-1], arr[ind]
            # print(ans,arr,x)
        return ans

        
