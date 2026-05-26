class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        s = set(word)

        for ch in s:
            if ch.islower() and ch.upper() in s:
                ans += 1

        return ans