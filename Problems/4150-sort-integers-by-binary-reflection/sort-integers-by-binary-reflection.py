class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflect(n):
            if n == 0: return 0
            return int(bin(n)[2:][::-1], 2)
        return sorted(nums, key=lambda x: (reflect(x), x))