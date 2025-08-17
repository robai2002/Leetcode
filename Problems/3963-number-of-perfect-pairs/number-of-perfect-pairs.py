from typing import List

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
       
        arr = sorted(abs(x) for x in nums)
        n = len(arr)
        j = 0
        ans = 0


        for i in range(n):
            while j < n and arr[j] <= 2 * arr[i]:
                j += 1
            ans += (j - i - 1)

        return ans
