class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 1
        y = 1 
        for i in nums:
            if y <1:
                return False
            y -= 1
            x = max(x-1,i)
            if y == 0:
                y = x
        return True