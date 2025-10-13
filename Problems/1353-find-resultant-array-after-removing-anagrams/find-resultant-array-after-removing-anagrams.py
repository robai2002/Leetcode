class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for word in words[1:]:
            if Counter(word) != Counter(ans[-1]):ans.append(word)
        return ans
