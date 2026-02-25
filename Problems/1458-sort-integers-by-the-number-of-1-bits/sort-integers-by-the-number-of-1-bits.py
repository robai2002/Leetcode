class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr1 = [bin(x)[2:].count('1') for x in arr]
        arr1 = [(x,y) for x,y in zip(arr1,arr)]
        arr1.sort()
        return [x for y,x in arr1]
        