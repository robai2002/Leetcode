class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [list(g)[0] for _, g in groupby(words, sorted)]