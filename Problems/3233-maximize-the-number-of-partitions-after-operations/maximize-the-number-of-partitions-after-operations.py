class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def dp(index: int, current_set: int, can_change: bool) -> int:
            if index == n:
                return 0

            ch_idx = ord(s[index]) - ord('a')
            updated_set = current_set | (1 << ch_idx)
            distinct_count = bin(updated_set).count("1")

            if distinct_count > k:
                res = 1 + dp(index + 1, 1 << ch_idx, can_change)
            else:
                res = dp(index + 1, updated_set, can_change)

            if can_change:
                for new_char in range(26):
                    new_set = current_set | (1 << new_char)
                    new_distinct = bin(new_set).count("1")
                    if new_distinct > k:
                        res = max(res, 1 + dp(index + 1, 1 << new_char, False))
                    else:
                        res = max(res, dp(index + 1, new_set, False))

            return res

        return dp(0, 0, True) + 1