from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endofWord = True  # ✅ FIXED

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        res = set() 
        visit = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visit or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endofWord:
                res.add(word)
                node.endofWord = False 

    
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r, c))

      
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")

        return list(res)
