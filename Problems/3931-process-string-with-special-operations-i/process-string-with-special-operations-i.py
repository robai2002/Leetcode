class Solution:
    def processStr(self, s: str) -> str:
        l = []
        for ch in s:
            if 'a'<=ch<='z':
                l.append(ch)
            elif l:
                if ch =='*':
                    l.pop()
                elif ch =='#':
                    l[:] = l[:] + l[:]
                elif ch == '%':
                    l = l[::-1]

        return ''.join(l)