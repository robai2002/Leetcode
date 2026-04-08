class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        even,n = 0,len(nums)
        dp = [0]*n
        for i in range(1,n-1,2):
            dp[i] = max(0,max(nums[i-1],nums[i+1])-nums[i]+1)
            dp[i] += 0 if i-2<0 else dp[i-2]
        if n&1:
            return dp[-2] 
        ans = dp[-3]
        # print(ans)
        for i in reversed(range(2,n-1,2)):
            even += max(0,max(nums[i-1],nums[i+1])-nums[i]+1)
            ans = min(ans,even + (0 if i-3<0 else dp[i-3]))
        return ans
            

        