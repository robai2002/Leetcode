class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for ind,num in enumerate(nums,start = 1):
            ans = max(ans,num+nums[-ind])
        return ans