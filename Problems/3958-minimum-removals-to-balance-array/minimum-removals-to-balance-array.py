class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        ans = 1
        while j<len(nums):
            
            if nums[i]*k<nums[j]:
                i+= 1
            else:
                j+= 1
                ans = max(ans,j-i)
     
        return len(nums)-ans
        