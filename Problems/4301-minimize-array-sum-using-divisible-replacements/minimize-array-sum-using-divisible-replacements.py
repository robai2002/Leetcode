class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        M = max(nums)+2
        arr = [i for i in range(M)]
        s = set(nums)
        for v in s:
            for i in range(v,M,v):
                arr[i] = min(arr[i],v)
        return sum(arr[i] for i in nums)

        