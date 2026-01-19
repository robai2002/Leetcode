class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]

        for ch in s:
            if ch.isalpha():
                ans = [x + ch.lower() for x in ans] + \
                      [x + ch.upper() for x in ans]
            else:
                ans = [x + ch for x in ans]

        return ans
