class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        l = list(c.values())
        ans = 0 
        l.sort(reverse = True)
        for ind,num in enumerate(l,8):
            ans += (ind//8)*num
        return ans