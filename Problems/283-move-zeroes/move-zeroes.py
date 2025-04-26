class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        for _,v in enumerate(nums):
            nums[_] = 0
            if v:
                nums[i] = v
                i += 1
        
