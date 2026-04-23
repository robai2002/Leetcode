class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0]*n
        mp = dict()
        cnt = dict()
        for ind,num in enumerate(nums):
            dp[ind] = cnt.get(num,0)*ind - mp.get(num,0)
            mp[num] = mp.get(num,0) + ind
            cnt[num] = cnt.get(num,0) + 1
        
        mp.clear()
        cnt.clear()

        for ind,num in reversed(list(enumerate(nums))):
            dp[ind] += cnt.get(num,0)*(n-ind-1) - mp.get(num,0)
            # dp[ind] = cnt.get(num,0)*ind - mp.get(num,0)
            mp[num] = mp.get(num,0) + (n-ind-1)
            cnt[num] = cnt.get(num,0) + 1
        return dp