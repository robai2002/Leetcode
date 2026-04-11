class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = dict()
        mp1 = dict()
        ans = len(nums)*3
        for i,num in enumerate(nums):
            if num in mp1:
                ans = min(ans,i-mp1[num])
            if num in mp:
                mp1[num] = mp[num]
            mp[num] = i
        return 2*ans if ans<=len(nums) else -1   