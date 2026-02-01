class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums= sorted(nums[1:])
        return ans + sum(nums[:2])