class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        n//=3
        l = nums[2*n:]
        print(l)
        heapify(l)
        s = sum(nums[2*n:])
        for i in reversed(range(n-1,2*n)):
            d[i] = s
            s+= nums[i]
            heapq.heappush(l,nums[i])
            s -= heapq.heappop(l)
        s =0
        l = []
        ans = 10**10
        for i in range(2*n):
            s+= nums[i]
            heapq.heappush(l,-nums[i])
            if len(l)>n:
                s += heapq.heappop(l)
            if i <n-1:
                continue
            ans = min(ans,s-d[i])
        return ans