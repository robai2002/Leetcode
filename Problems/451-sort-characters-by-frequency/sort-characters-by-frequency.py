class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = list(s)
        s.sort(key = lambda ch:(-c[ch],ch))
        return "".join(s)
        