class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        @cache
        def get_val(n: int, val: int) -> list[int]:
            nonlocal k
            ans = []
            if n == 1:
                if val > 0:
                    return [val]
                return []
            if val - k >= 0:
                for x in get_val(n - 1, val - k):
                    ans.append(x * 10 + val)
            if val + k < 10 and k!=0:
                for x in get_val(n - 1, val + k):
                    ans.append(x * 10 + val)

            return ans

        result = []
        for i in range(10):
            l = get_val(n, i)
            for v in l:
                result.append(v)
        return result
