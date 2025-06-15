class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def marge_sort(start: int,end: int) ->int:

            # base case 
            if start>=end:
                return 0
            
            # divide 
            mid = (start+end)//2
            count = marge_sort(start,mid) + marge_sort(mid+1,end)

            i,j = start,mid+1
            # two pointer
            while i<=mid and j<=end:
                if nums[i]>2*nums[j]:
                    count += mid-i+1
                    j += 1
                else:
                    i += 1
            
            # marge two sorted halves
            nums[start:end+1] = sorted(nums[start:end+1])

            return count
        
        return marge_sort(0,len(nums)-1)