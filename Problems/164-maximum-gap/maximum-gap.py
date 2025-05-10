class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxs=0
        for i in range(len(nums)-1):
            tot=nums[i+1]-nums[i]
            if(maxs<tot):
                maxs=tot;
        return maxs       
        