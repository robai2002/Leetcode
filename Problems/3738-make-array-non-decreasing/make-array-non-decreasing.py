class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans,mx = 0,0
        for num in nums:
            if mx<=num:
                ans += 1
                mx = num
        return ans
        