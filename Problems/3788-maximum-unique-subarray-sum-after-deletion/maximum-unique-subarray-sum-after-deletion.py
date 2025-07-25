class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m = max(nums)
        if m<0:
            return m
        s = set()
        for num in nums:
            if num>0:
                s.add(num)
        ans = 0
        for num in s:
            ans += num
        return ans