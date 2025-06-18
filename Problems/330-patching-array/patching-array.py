class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ind = 0
        x,c = 0,0
        while x<n:
            if ind<len(nums) and nums[ind]<x+2:
                x+= nums[ind]
                ind += 1
            else:
                x += x+1
                c += 1
        return c 