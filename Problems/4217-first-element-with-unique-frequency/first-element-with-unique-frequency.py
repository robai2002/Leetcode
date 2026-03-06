class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c = Counter(nums)
        x = Counter(c.values())
        for num in c.keys():
            if x[c[num]] == 1:
                return num
        return -1
        