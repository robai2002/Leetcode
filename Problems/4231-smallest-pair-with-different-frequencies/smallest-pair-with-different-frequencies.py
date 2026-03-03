class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        arr = list(c.keys())
        arr.sort()
        val = arr[0]
        for i in range(1,len(arr)):
            if c[val]!=c[arr[i]]:
                return [val,arr[i]]


        return [-1,-1]
        