class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in reversed(nums):
            while num:
                ans.append(num%10)
                num//=10
        return ans[::-1]