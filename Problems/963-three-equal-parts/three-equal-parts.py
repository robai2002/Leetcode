class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ind = [i for i,x in enumerate(arr) if x]
        n, r  = divmod(len(ind), 3)
        if r:
            return [-1, -1]
        if not n:
            return [0,2]
        l = len(arr)-ind[-n]
        if arr[ind[0]:ind[0]+l] == arr[ind[n]:ind[n]+l] == arr[ind[-n]:ind[-n]+l]:
            return [ind[0]+l-1,ind[n]+l]
        return [-1,-1]