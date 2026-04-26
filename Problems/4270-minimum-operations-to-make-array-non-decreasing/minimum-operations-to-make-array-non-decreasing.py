class Solution:
    def minOperations(self, nums: list[int]) -> int:
        hand = 0
        ans = 0 
        prev = 0
        for num in nums:
            if num>=prev:
                hand = 0
            if num<prev:
                ans += max(prev-num - hand,0)
                hand = prev -num
            prev = max(num,prev)
        return ans
        