class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        q = 0
        for ind,num in enumerate(nums,start=-1):
            if ind <0: continue
            if nums[ind]>=num:
                q = ind + 1
        p = len(nums)
        for ind, num in reversed(list(enumerate(nums))):
            if ind == 0:continue
            if nums[ind-1]>=num:
                p = ind-1
        if p<1 or q+2>len(nums):
            return False
        r = 1
        for i in range(2,len(nums)-1):
            if nums[i-1]<=nums[i]:
                r = i
           # print(p+1<=r ,i+1>=q,i-r,p,q,r,i)
            if p>=r and i>=q and i-r>0:
                return True

        return False
