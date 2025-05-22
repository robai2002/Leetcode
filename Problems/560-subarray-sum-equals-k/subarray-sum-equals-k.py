class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {}
        x = 0
        ans = 0 
        for v in nums:
            if x in m: m[x] += 1
            else: m[x] = 1
            x += v
            if x-k in m: ans+=m[x-k]
        return ans