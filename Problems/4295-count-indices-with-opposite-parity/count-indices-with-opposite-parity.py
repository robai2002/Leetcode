class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        odd, even = 0, 0
        for i in reversed(range(n)):
            if nums[i]%2:
                odd += 1
                nums[i] = even
            else:
                even += 1
                nums[i] = odd
        return nums
        