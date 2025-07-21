class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for ch in s:
            if len(ans)<2 or ans[-1]!=ch or ans[-2]!=ch:
                ans.append(ch)
        return "".join(ans)