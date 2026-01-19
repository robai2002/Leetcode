class Solution:
    def customSortString(self, order: str, s: str) -> str:
        l = list(s)
        mp = dict()
        for ind,ch in enumerate(order,start = 1):
            mp[ch] = ind
        def heapify(ind: int,n: int) ->None:
            largest = ind
            if ind*2+1<n and mp.get(l[largest],0)< mp.get(l[ind*2+1],0):
                largest = ind*2+1
            
            if ind*2+2<n and mp.get(l[largest],0)< mp.get(l[ind*2+2],0):
                largest = ind*2+2
            if ind!=largest:
                l[ind],l[largest] = l[largest],l[ind]
                heapify(largest,n)
            return




        def heap_sort():
            for i in range(len(l) // 2 - 1, -1, -1):
                heapify(i,len(l))
            for i in range(len(l)-1,0,-1):
                l[0],l[i] = l[i],l[0]
                heapify(0,i)
            return l

        
        return "".join(heap_sort())
