class TrieNode:
    def __init__(self):
        self.child = {}
        self.length = 10**6
        self.index = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int, length: int) -> None:
        if self.root.length>length:
            self.root.length = length
            self.root.index = index
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
                curr.child[ch].index = index
                curr.child[ch].length = len(word)
            elif curr.child[ch].length > length:
                curr.child[ch].index = index
                curr.child[ch].length = length
            curr = curr.child[ch]

    def search(self, word: str, length: int) -> int:
        curr = self.root
        for ch in word:
            if ch in curr.child:
                curr = curr.child[ch]
            else:
                break
        return curr.index

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie()
        for index, word in enumerate(wordsContainer):
            trie.insert(word[::-1], index, len(word)) 
        
        return [trie.search(word[::-1], len(word)) for word in wordsQuery]