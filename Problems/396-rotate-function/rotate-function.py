class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = 0
        d = 0
        for ind,num in enumerate(nums):
            d +=ind*num
        ans = d
        n = len(nums)
        for num in reversed(nums):
            d += s - n*num
           
            ans = max(ans,d)
        return ans 

        