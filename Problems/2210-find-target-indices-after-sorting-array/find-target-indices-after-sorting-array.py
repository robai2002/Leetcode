class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        x,c =0,0
        for num in nums:
            if num<target:
                x += 1
            if num == target:
                c += 1
        return [x+y for y in range(c)]
        