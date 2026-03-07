class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if (max(nums) - min(nums)) * n <= k:
            return n * (n + 1) // 2

        l = 0
        r = 0
        mn, mx = deque(), deque()
        res = 0
        while r < len(nums):
            while mx and mx[-1] < nums[r]:
                mx.pop()
            mx.append(nums[r])

            while mn and mn[-1] > nums[r]:
                mn.pop()
            mn.append(nums[r])

            while (mx[0] - mn[0]) * (r-l+1) > k:
                if nums[l] == mx[0]:
                    mx.popleft()
                if nums[l] == mn[0]:
                    mn.popleft()
                l += 1

            res += r-l+1
            r += 1
        return res