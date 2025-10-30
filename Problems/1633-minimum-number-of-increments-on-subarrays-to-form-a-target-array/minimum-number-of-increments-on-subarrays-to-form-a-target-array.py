class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        mx = 0
        for num in target:
            if num>=mx:
                ans += num - mx
                mx = num
            else:
                mx = num
        return ans
        