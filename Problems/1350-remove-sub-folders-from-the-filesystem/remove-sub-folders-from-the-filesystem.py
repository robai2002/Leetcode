class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.endofFolder = False

class Trie:
    def __init__(self):
        self.root = TrieNode("/")
        self.ans = []
        self.road = []

    def insert(self, path):
        curr = self.root
        for c in path:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.endofFolder = True

    def get_ans(self, node):
        if node != self.root:
            self.road.append(node.name)

        if node.endofFolder:
            self.ans.append("/" + "/".join(self.road))
            if node != self.root:
                self.road.pop()
            return

        for child in node.children.values():
            self.get_ans(child)

        if node != self.root:
            self.road.pop()

class Solution:
    def removeSubfolders(self, folder):
        R = Trie()
        for s in folder:
            s = s.split("/")[1:]  
            R.insert(s)
        R.get_ans(R.root)
        return R.ans
