class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        temp = []
        for ind,num in enumerate(nums):
            temp.append((num,ind))
        temp.sort()
        i,j,n = 0,0,len(nums)
        
       
        while i<n:
            print(i)
            ind = [temp[i][1]]
            j = i + 1
            while j<n and temp[j][0] - temp[j-1][0] <= limit:
                ind.append(temp[j][1])
                j += 1 
            ind.sort(reverse = True)
            print(ind)
            while ind:
                x = ind.pop()  
                nums[x] = temp[i][0]
                i += 1
        return nums 
        