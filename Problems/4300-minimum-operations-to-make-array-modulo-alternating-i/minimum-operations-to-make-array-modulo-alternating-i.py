class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        def get_cost(nums, t):
            return sum(min((t - x) % k, (x - t) % k) for x in nums)

        def solve(nums):
            n = len(nums)
            nums = sorted(x % k for x in nums)
            
            a = nums + [x + k for x in nums]
            ps = list(accumulate(a, initial=0))

            mn = inf
            res = -1
            for l in range(n):
                r = l + n
                mid = (l + r) // 2
                x = a[mid]
                
                cost = (x * (mid - l) - (ps[mid] - ps[l]) +
                       (ps[r] - ps[mid]) - x * (r - mid))
                
                if cost < mn:
                    mn = cost
                    res = x % k
                elif cost == mn and x % k != res:
                    res = -1

            if res == -1:
                return -1, mn, mn

            second = min(get_cost(nums, (res - 1) % k),
                         get_cost(nums, (res + 1) % k))
            return res, mn, second

        x, x_top1, x_top2 = solve(nums[::2])
        y, y_top1, y_top2 = solve(nums[1::2])

        if x == y != -1:
            return min(x_top1 + y_top2, x_top2 + y_top1)
        else:
            return x_top1 + y_top1