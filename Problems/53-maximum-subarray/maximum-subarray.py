class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        if ans<0:
            return ans
        x = 0
        for v in nums:
            x += v
            x = max(0,x)
            ans = max(ans,x)
        return ans