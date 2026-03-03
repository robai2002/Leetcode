class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        arr = list(c.keys())
        arr.sort()
        for ind,val in enumerate(arr):
            for i in range(ind+1,len(arr)):
                if c[val]!=c[arr[i]]:
                    return [val,arr[i]]


        return [-1,-1]
        