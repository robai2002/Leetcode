class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
         s = s.split()
         return len(set(s)) == len(set(p)) == len(set(zip_longest(s,p)))
         
        