class Solution:
    def minArraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = 0
        best = [float('inf')] * k
        best[0] = 0
        prefix = 0
        for x in nums:
            prefix = (prefix + x) % k
            keep = dp + x
            cut = best[prefix]
            dp = keep if keep < cut else cut
            if dp < best[prefix]:
                best[prefix] = dp
        return dp