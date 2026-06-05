class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x: int) -> int:
            if x <= 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos, tight, started, prev_digit, prev_cmp):
                if pos == n:
                    return (1, 0)  # count, waviness_sum

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, 0, 0)
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    if not started:
                        cnt, wav = dfs(pos + 1, ntight, True, d, 0)
                    else:
                        cmp_now = (d > prev_digit) - (d < prev_digit)

                        add = 1 if prev_cmp and cmp_now and prev_cmp != cmp_now else 0

                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            cmp_now
                        )

                        wav += add * cnt

                    total_cnt += cnt
                    total_wav += wav

                return total_cnt, total_wav

            return dfs(0, True, False, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)