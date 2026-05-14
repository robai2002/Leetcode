class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        for ind,num in enumerate(nums,1):
            if ind>n and num==n:
                return True
            elif ind!=num:
                return False
        return False
                
        