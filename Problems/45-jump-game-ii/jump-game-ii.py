class Solution:
    def jump(self, nums: List[int]) -> int:
        x = 1
        y = 0
        ans = 0
        for i in range(len(nums)):
            if y<i:
                ans += 1
                y = x
            x = max(x,i+nums[i])
        return ans
            
