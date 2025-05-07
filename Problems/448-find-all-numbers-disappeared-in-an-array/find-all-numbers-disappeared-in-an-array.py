class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i+1 for i in range(len(nums)) if i+1 not in s]