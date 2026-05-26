class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        d = dict()
        for num in nums:
            d[num] = d.get(num,0)
            if d[num]<k:ans.append(num)
            d[num] += 1
        return ans
        