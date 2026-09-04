class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        mx,mn = -10**12, 10**12
        n = len(nums)
        dp = [mn]*n
        n = len(nums)-1
        for ind,num in enumerate(nums[::-1]):
            mn = min(mn,num)
            dp[n-ind] = mn
        for ind,num in enumerate(nums):
            mx = max(mx,num)
            if mx - dp[ind]<=k:
                return ind
        return -1
            
            
        return -1
            