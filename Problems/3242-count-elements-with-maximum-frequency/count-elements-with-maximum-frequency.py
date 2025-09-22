import collections as C
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = C.Counter(nums)
        m,ans=0,0
        for value in c.values():
            if value>m:
                m,ans=value,1
            elif value == m:
                ans += 1
        return ans*m
        