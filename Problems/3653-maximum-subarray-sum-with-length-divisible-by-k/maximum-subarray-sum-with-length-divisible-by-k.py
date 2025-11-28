class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[k-1] = 0
        x = 0
        ans = -10**15
        for ind,num in enumerate(nums):
            ind%=k
            x += num
            if ind in d:
                ans = max(ans,x-d[ind])
                d[ind] = min(d[ind],x)
            else:
                d[ind] = x
            print(ind,ans)
        return ans