class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        dpl = [0 for i in range(n)]
        dpr = [n-1  for i in range(n)]
        pref = list(accumulate(nums))
        lpref = [0 for i in range(n)]
        rpref = [0 for i in range(n)]

        
        p = 0 
        for ind,num in enumerate(nums[1:]):
            if nums[ind]>=num:
                p = ind+1
            dpl[ind+1] = p
        
        for i in range(n):
            z = nums[i]
            if dpl[i]!=i:
                z += lpref[i-1]
            lpref[i] = max(lpref[i],z)
        
            


        p = n-1
        for i in reversed(range(n-1)):
            if nums[i]>=nums[i+1]:
                p = i
            dpr[i] = p

        for i in reversed(range(n)):
            z = nums[i]
            if dpr[i]!=i:
                z += rpref[i+1]
            rpref[i] = max(z,0)

        s = 0
        ans = -10**16
        for i in range(1,n-1):
            if nums[i-1]<=nums[i]:
                s = i
            elif dpl[s]==s:
                s += 1
            elif dpr[i]>i:
                z = pref[i+1]
                if s-1>0:
                    z -= pref[s-2]
                if dpr[i]>i+1:
                    z+= rpref[i+2]
                if dpl[s]<s-1:
                    z += lpref[s-2]
                
                ans = max(ans,z)
                print(i,ans,dpr[i])
        
    


        return ans
        