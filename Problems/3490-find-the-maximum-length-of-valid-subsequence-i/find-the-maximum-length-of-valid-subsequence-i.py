class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd,even,alter =0,0,0
        need = nums[0]%2
        for num in nums:
            if num&1:
                odd += 1
            else:
                even += 1
            if num%2 == need:
                need^=1
                alter += 1
        return max(odd,even,alter)