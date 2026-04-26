class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        A = set([0, n - 1])

        l = nums[0]
        for i in range(1, n):
            if nums[i] > l: A.add(i)
            l = max(l, nums[i])

        r = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] > r: A.add(i)
            r = max(r, nums[i])

        return [nums[i] for i in sorted(A)]