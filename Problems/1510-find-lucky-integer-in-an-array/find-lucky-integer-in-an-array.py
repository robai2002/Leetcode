class Solution:
    def findLucky(self, arr: List[int]) -> int:
        store = {}
        luckyNumbers = []
        
        for x in arr:
            if x not in store:
                store[x] = 1
            else:
                store[x] = store[x] + 1
        
        for key,value in store.items():
            if key == value:
                luckyNumbers.append(key)
        
    
        if not luckyNumbers:
            return -1
        else:
            return max(luckyNumbers)
