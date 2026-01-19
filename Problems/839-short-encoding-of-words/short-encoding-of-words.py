class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: -len(x))
        ans = 0
        for i in range(len(words)):
            c = len(words[i])+1
            for j in range(i):
                if words[j][-(len(words[i])):] == words[i]:
                    c = 0 
                    break
            ans+= c
        return ans
