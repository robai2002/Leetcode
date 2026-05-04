n = 10000
arr = [i for i in range(n)]
arr[1] = 0
for i in range(2,n):
    if arr[i]==i:
        for j in range(i*i,n,i):
            arr[j] = 0
    arr[i]+= arr[i-1]


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        if n==0:return 0
        m = int(str(n)[::-1])
        for i in range(n):
            print(i,arr[i])
        if m<n:
            return arr[n] - arr[m-1]
        else:
            return arr[m] - arr[n-1]