class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        decimal_nos = set()

        for num in nums:
            decimal_nos.add(int(num, 2))

        for i in range(2**n):
            if i not in decimal_nos:
                return format(i, f'0{n}b')