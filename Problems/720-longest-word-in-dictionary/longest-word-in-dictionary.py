class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.endofWord = True

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofWord = True

    def get_max(self, node=None, w='1'):
        if node is None:
            node = self.root
        ans = ""
        if not node.endofWord:
            return ""
        for c in node.children:
            s = self.get_max(node.children[c], c)
            if len(s) > len(ans):
                ans = s
            elif len(s) == len(ans):
                ans = min(ans, s)
        return w + ans


class Solution:
    def longestWord(self, words: list[str]) -> str:
        x = Trie()
        for word in words:
            x.insert(word)
        return x.get_max()[1:]
