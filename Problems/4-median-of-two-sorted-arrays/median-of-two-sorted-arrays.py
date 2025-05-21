class Solution:
    def helper(self, a , b):
        l = []
        if len(a) == 0:
            x = (len(b)-1)//2
            for i in range(x,min(len(b),x+2)):
                l.append(b[i])
            return sorted(l)
        x = (len(a)+len(b)+1)//2
        i = 0
        j = min(len(a),x-1)
        while i<j:
            m =(i+j+1)//2
            if a[m-1]<=b[x-m -1]:
                i = m
            else:
                j = m - 1
        for ii in range(i ,min(len(a),i+2)):
            l.append(a[ii])
        j = x - i-1
        for ii in range(j,min(len(b),j+2)):
            l.append(b[ii])
        return sorted(l)


    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a)>len(b):
            a,b=b,a
        ll = self.helper(a,b)
        if (len(a)+len(b))%2:
            return ll[0]
        return (ll[0]+ll[1])/2