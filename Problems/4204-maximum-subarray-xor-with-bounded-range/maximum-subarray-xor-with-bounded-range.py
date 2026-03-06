class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.zero = 0
        self.one = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert the value in the trie
    def insert(self, key):
        curr = self.root

        for i in reversed(range(30)):
            if (1<<i)&key>0: # key value one at (1<<i) bits
                
                curr.one += 1
                # print((1<<i),key,curr.zero,curr.one," one")
                if curr.children[1] == None:
                    curr.children[1] = TrieNode()
                curr = curr.children[1] 
            else:
                
                curr.zero += 1
                # print((1<<i),key,curr.zero,curr.one," zero")
                if curr.children[0] == None:
                    curr.children[0] = TrieNode()
                curr = curr.children[0]
        return  
    def search(self, key):
        curr = self.root
        ans = 0

        for i in reversed(range(30)):
            if (1<<i)&key == 0 and curr.one>0: # key value one at (1<<i) bits
                
                curr = curr.children[1] 
                ans |= (1<<i)
                # print((1<<i),key,curr.zero,curr.one,"zero")

            elif (1<<i)&key>0 and curr.zero>0:
                ans |= (1<<i) 
                # print((1<<i),key,curr.zero,curr.one,"one")
                curr = curr.children[0]
            else:
                curr = curr.children[1]  if curr.one>0 else curr.children[0] 
           
        return  ans

    # Remove the value from trie
    def remove(self, key):
        curr = self.root

        for i in reversed(range(30)):

            if (1<<i)&key>0: # key value one at (1<<i) bits
                
                curr.one -= 1
                curr = curr.children[1] 
            else:
                
                curr.zero -= 1
                curr = curr.children[0]      
        return  

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        prefix = [0]
        mx = deque()
        mn = deque()
        l = 0
        trie = Trie()
        trie.insert(0)

        result = 0

        for ind,num in enumerate(nums,start =1):
            
            while mx and mx[-1]<num:mx.pop()

            while mn and mn[-1]>num:mn.pop()

            mx.append(num)
            mn.append(num)
            prefix.append(prefix[-1]^num)
            trie.insert(prefix[-1])

            while mx[0] - mn[0]>k:
                if mx[0] == nums[l]:mx.popleft()
                if mn[0] == nums[l]:mn.popleft()
                
                trie.remove(prefix[l])
                l += 1
       
            result = max(result,trie.search(prefix[-1]))


        return result



        