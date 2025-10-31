class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [key for key,value in c.items() if value>1]
        