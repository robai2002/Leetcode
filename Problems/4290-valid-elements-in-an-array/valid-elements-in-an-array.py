class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        dp = [0]*n
        mx = 0
        for ind,num in enumerate(nums):
            if num>mx:
                dp[ind] = num
                mx = num
        mx = 0
        for ind,num in reversed(list(enumerate(nums))):
            if num>mx:
                dp[ind] = num 
                mx = num
        return [num for num in dp if num>0]
        