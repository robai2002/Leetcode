class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x,y =-1,-1
        ans = 0
        for i,v in enumerate(nums):
            if v:
                ans = max(ans,max(i-x-1,i-y))
            else:
                x = y
                y = i
        return min(len(nums)-1,ans)