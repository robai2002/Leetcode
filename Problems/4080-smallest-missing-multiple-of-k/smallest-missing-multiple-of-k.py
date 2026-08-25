class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x = k
        while k in nums:k+=x
        return k
        