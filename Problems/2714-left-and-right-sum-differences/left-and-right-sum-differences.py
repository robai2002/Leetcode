class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l,r = 0,sum(nums)
        for ind,num in enumerate(nums):
            r-=num
            nums[ind] = abs(l-r)
            l += num
        return nums

