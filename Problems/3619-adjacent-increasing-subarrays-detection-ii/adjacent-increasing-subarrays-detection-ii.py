class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dpf = [0 for i in range(n)]
        dpb = [0 for i in range(n)]
        c = 0 
        for ind,num in enumerate(nums):
            if ind>0 and num>nums[ind-1]:
                c += 1
            else:
                c = 1
            dpf[ind] = c

        c = 0
        for ind in reversed(range(n)):
            if ind<n-1 and nums[ind]<nums[ind+1]:
                c += 1
            else:
                c = 1
            dpb[ind] = c
        c = 1
        for i in range(n-1):
            c = max(c,min(dpf[i],dpb[i+1]))
        
        return c
            
