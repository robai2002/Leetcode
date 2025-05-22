class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()#O(nlog(n))
        return nums[len(nums)//2]