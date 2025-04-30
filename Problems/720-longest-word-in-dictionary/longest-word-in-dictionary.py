class Solution:
    def longestWord(self, words: List[str]) -> str:
        visited = set()
        visited.add("")
        words.sort()
        res = ""
        for word in words:
            if word[:-1] in visited:
                visited.add(word)
                if len(res) < len(word):
                    res = word

        return res