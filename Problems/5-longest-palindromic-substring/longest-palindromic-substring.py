class Solution:
    def find_string(self, s, l, g, current_ind, current_ans):
        ind = -1
        ans = -1
        for i in range(len(s) - g + 1):
            if l[i + 1] == g - 2 and s[i] == s[i + g - 1]:
                l[i] = g
                ans = g
                ind = i
        return (current_ind, current_ans) if ans == -1 else (ind, ans)

    def longestPalindrome(self, s: str) -> str:
        v = len(s)
        l = [1] * v
        ll = [0] * v
        ind = 0
        ans = 1

        for iii in range(2, v + 1):
            if iii % 2:
                ind, ans = self.find_string(s, l, iii, ind, ans)
            else:
                ind, ans = self.find_string(s, ll, iii, ind, ans)
            if ans + 2 < iii:
                break

        sss = []
        for i in range(ind, ind + ans):
            sss.append(s[i])
        return ''.join(sss)


