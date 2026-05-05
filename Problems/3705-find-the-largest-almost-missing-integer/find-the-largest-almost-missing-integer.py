class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums)==k:return max(nums)
        ans = -1
        if k ==1: 
            return max((key for key,value in Counter(nums).items() if value == 1), default=-1)
        if nums.count(nums[0])==1:
            ans = nums[0]
        if nums.count(nums[-1])==1:
            ans = max(nums[-1],ans)
        
        return ans