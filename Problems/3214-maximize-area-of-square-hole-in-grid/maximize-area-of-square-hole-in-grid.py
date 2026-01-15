class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def get_max(arr: List[int])->int:
            ans = 2
            cnt,prev  = 1,1
            for num in arr:
                if num-1==prev:
                    cnt += 1
                else:
                    cnt = 2
                prev = num
                ans = max(cnt,ans)
            return ans
        return min(get_max(sorted(hBars)),get_max(sorted(vBars)))**2
