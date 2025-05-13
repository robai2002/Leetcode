from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        C = Counter(p)
        m = defaultdict(int)
        ans = []
        left = 0
        matched = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in C:
                m[ch] += 1
                if m[ch] == C[ch]:
                    matched += 1
            
            while right - left + 1 > len(p):
                if s[left] in C:
                    if m[s[left]] == C[s[left]]:
                        matched -= 1
                    m[s[left]] -= 1
                left += 1
        
            if matched == len(C):
                ans.append(left)
        return ans
