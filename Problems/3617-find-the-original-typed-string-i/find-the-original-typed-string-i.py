class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        for i,ch in enumerate(word):
            if i==0 or ch == word[i-1]:
                ans += 1
        return ans