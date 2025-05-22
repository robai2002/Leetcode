from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        required = len(t)
        left = 0
        right = 0
        window_count = Counter()
        ans = float('inf')
        ans_left = 0        
        while right < len(s):
            window_count[s[right]] += 1
            if window_count[s[right]] <= c[s[right]]:
                required -= 1
            while required == 0:
                if right - left + 1 < ans:
                    ans = right - left + 1
                    ans_left = left
                window_count[s[left]] -= 1
                if window_count[s[left]] < c[s[left]]:
                    required += 1
                left += 1
            right += 1
        if ans == float('inf'):
            return ""
        return s[ans_left: ans_left + ans]
