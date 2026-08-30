class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mx,mn = max(nums), min(nums)
        
        mi,mni = nums.index(mn), nums.index(mx)
        
        n = len(nums)
        
        if mi<mni:
            mi,mni = mni, mi
    
        return min([mi+1, n-mni, n - mi + mni +1])
