class TrieNode:
    def __init__(self):
        self.children = {}
        self.arr = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def make_list(self,word):
        cur = self.root
        for c in word:
            cur.children[c] = TrieNode()
            cur = cur.children[c]
        
    def insert(self,word):
        cur =self.root
        for c in word:
            if c in cur.children:
                if len(cur.arr)<3:
                    cur.arr.append(word)
            else:
                return 
            cur = cur.children[c]
        return 
    
    def get_ans(self,word):
        cur = self.root
        ans = []
        for c in word:
            ans.append(cur.arr)
            cur = cur.children[c]
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        trie = Trie()
        trie.make_list(word)
        for p in sorted(products):
            trie.insert(p)
        return trie.get_ans(word)