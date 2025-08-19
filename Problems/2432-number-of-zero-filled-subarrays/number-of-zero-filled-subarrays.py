class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans,x = 0,0
        for v in nums:
            x = 0 if v else x+1
            ans += x
        return ans