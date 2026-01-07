class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for ind,l in enumerate(nums):
            for num in l:
                arr.append((num,ind))
        arr.sort()
        ind,c =0,len(nums)
        ans,st = 10**10,0
        dp = [0 for i in range(c)]
        for x,y in arr:
            if dp[y]==0:
                c -= 1
            dp[y] += 1
            if c>0:continue
            while dp[arr[ind][1]]>1:
                dp[arr[ind][1]]-=1
                ind += 1
            
            if x-arr[ind][0]<ans:
                ans = x-arr[ind][0]
                st = arr[ind][0]
        
        return [st,st+ans]
            

            

