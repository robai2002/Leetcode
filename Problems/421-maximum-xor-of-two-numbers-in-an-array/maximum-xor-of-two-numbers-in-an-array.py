class TrieNode:
    def __init__(self):
        self.children = [None, None]  # Instead of dict


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        cur = self.root
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]

    def search(self, num):
        cur = self.root
        xor_sum = 0
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if cur.children[toggled]:
                xor_sum |= (1 << i)
                cur = cur.children[toggled]
            else:
                cur = cur.children[bit]
        return xor_sum


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_xor = 0
        trie.insert(nums[0])
        for num in nums[1:]:
            max_xor = max(max_xor, trie.search(num))
            trie.insert(num)
        return max_xor
