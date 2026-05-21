class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}
            
        class Trie:
            def __init__(self):
                self.root = TrieNode()

            
            def insert(self,word:int) -> None:
                node = self.root
                for ch in str(word):
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]

            def search(self,word: int) -> int:
                ans = 0
                node = self.root
                for ch in str(word):
                    if ch not in node.children:
                        return ans
                    ans += 1
                    node = node.children[ch]
                return ans
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        return max(trie.search(num) for num in arr2)

