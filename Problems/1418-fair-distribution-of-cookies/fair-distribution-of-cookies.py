class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        l = [0 for i in range(k)]
        ans = 10**6
        def get_ans(ind: int) -> None:
            nonlocal ans
            if ans<max(l):
                return 
            if ind == len(cookies):
                ans = max(l)
                return
            for i in range(k):
                l[i] += cookies[ind]
                get_ans(ind + 1)
                l[i] -= cookies[ind]
            return
        get_ans(0)
        return ans
