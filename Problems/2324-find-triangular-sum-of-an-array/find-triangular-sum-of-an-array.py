class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        c = 1
        ans = 0
        for ind,num in enumerate(nums):
            ans +=c*num
            ans%=10
            c*=(n-ind-1)
            c//=(ind+1)
        return ans