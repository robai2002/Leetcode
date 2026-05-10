class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        dp[0]=0
        for ind,num in enumerate(nums):
            if dp[ind]==-1:continue
            for ind2,num2 in enumerate(nums[ind+1:],ind+1):
                if abs(num2-num)<=target:
                    dp[ind2] = max(dp[ind2],dp[ind]+1)
           # print(dp)
        return dp[-1]
        