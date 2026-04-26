from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
       
        extracted = [ch for ch in s if ch in vowels]
        c = Counter(s)
        extracted.sort(key = lambda ch:(-c[ch],s.index(ch)))
      
        res = []
        i = 0
        
        for ch in s:
            if ch in vowels:
                res.append(extracted[i])
                i += 1
            else:
                res.append(ch)
        
        return ''.join(res)