class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """   
        n = len(nums)
        def heapfiy(pos: int, limit: int) ->None:
            x,y = pos*2+1,pos*2+2
            z = pos
            if x<limit and nums[z]<nums[x]:
                z = x
            if y<limit and nums[z] <nums[y]:
                z = y
            
            if pos!=z:
                nums[pos],nums[z] = nums[z],nums[pos]
                heapfiy(z,limit)
            return 


        x = n//2 - 1
        while x>=0:
            heapfiy(x,n)
            x -= 1
        while n:
            n -= 1
            nums[0],nums[n] = nums[n],nums[0]
            heapfiy(0,n)
        return  
        