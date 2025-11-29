class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        d = dict()
        d[(0,0)] = -1
        oe = 0
        x = 0
        ans = 0
        for ind,num in enumerate(nums):
            x^=num
            if num&1:
                oe-=1
            else:
                oe += 1
            if (oe,x) in d:
                ans = max(ans,ind-d[(oe,x)])
            else:
                d[(oe,x)] = ind
        return ans
