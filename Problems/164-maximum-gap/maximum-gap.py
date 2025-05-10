class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        prv = 10**9
        s = set(nums)
        ans = 0
        for v in sorted(s):
            ans = max(ans,v-prv)
            print(ans,v,prv)
            prv = v
        return ans