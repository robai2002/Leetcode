class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums  + [1]
        @cache 
        def dp(l: int,h: int) -> int:
            if l>h:
                return 0
            x = 0
            for i in range(l,h+1):
                x = max(x,nums[l-1]*nums[i]*nums[h+1] + dp(l,i-1)+dp(i+1,h))
            return x
        
        return dp(1,len(nums) - 2)