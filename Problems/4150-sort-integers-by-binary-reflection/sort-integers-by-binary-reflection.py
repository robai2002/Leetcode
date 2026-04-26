class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        t=[]
        for i in nums:
            b=bin(i)[2:]
            r=b[::-1]
            reflect=int(r,2)
            t.append((reflect,i))
        t.sort()
        return [i for _,i in t]