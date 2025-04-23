class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def C(cap: int) -> bool:
            capacity = [cap] * k

            def backtracking(ind: int) -> bool:
                if ind == len(cookies):
                    return True
                for i in range(k):
                    if capacity[i] >= cookies[ind]:
                        capacity[i] -= cookies[ind]
                        if backtracking(ind + 1):
                            return True
                        capacity[i] += cookies[ind]
                return False

            return backtracking(0)

        def get_val(pos: int, amb: int) -> int:
            print(pos,amb)
            while pos < amb:
                mid = (pos + amb +1) // 2
                if C(mid):
                    amb = mid - 1
                else:
                    pos = mid
            return pos + 1

        return get_val(max(cookies)-1, sum(cookies))
