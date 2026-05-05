class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pref=list(accumulate(nums,initial=0))
        @cache
        def dp(i,k,can_extend):
            if n-i<k*m:
                return -inf
            if i == n:
                return 0 if k == 0 else -inf

            ans = dp(i+1,k,False)
            if can_extend:
                ans=max(ans,dp(i+1,k,True)+nums[i])
            if k > 0 and i+m<=n:
                ans = max(ans, dp(i+m,k-1,True)+pref[i+m]-pref[i])
            return ans   

        ans = dp(0,k,False)
        dp.cache_clear()
        return ans