class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        def get_ans(arr: List[int],x: int):
            prev = 1
            arr.extend([1,x])
            arr.sort()
            s = set()
            cnt = 1
            for ind,num in enumerate(arr):
                for v in arr[ind+1:]:
                    s.add(v-num)
            return s
        ans = get_ans(hFences,m)&get_ans(vFences,n)
        return max(ans)**2%(10**9+7) if ans else -1
