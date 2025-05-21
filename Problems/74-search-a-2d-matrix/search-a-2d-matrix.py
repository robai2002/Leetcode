class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        x = len(m[0])
        h= len(m)*x
        l =0 
        while l<h:
            mid =(h+l)//2
            if m[mid//x][mid%x]== target:
                return True
            if m[mid//x][mid%x]>target:
                h =mid
            else:
                l = mid + 1
            print(l, h)
        return False