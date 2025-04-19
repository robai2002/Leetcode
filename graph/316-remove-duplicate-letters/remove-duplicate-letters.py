class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        a = Counter(s)
        seen = set()
        l = []
        for c in s:
            a[c] -= 1
            if c in seen:continue
            while l and l[-1]>c and a[l[-1]]>0:
                seen.remove(l[-1])
                l.pop()
            seen.add(c)
            l.append(c)
        return ''.join(l)