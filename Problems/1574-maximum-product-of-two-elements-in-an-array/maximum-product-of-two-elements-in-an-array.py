class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx,mx2 = 0,0
        for num in nums:
            mx2 = max(mx2,num)
            if mx<mx2:
                mx2,mx = mx, mx2
        return mx2*mx -mx2 -mx +1