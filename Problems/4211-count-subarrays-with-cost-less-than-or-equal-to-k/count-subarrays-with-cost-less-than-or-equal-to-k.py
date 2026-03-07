class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = -1
        mx = deque()
        mn = deque()
        ans = len(nums)
        fin  = -1
        for ind,num in enumerate(nums):
           # print(mx,mn)
            while mx and nums[mx[-1]]<num: mx.pop()
            while mn and nums[mn[-1]]>num:
                print(nums[mn[-1]],num)
                mn.pop()
            mx.append(ind)
            mn.append(ind)
            #print(mx,mn,end =" done\n")
            
            while len(mx)>1 or len(mn)>1: 
                x = ind - min(mx[0],mn[0]) +1
                d =  (nums[mx[0]]-nums[mn[0]])
                z = ind-fin if d== 0 else min(ind-fin,k//d)
                #print(x,d,ind,fin,z)
                if z<x:
                    if mx[0]<mn[0]:
                        fin = mx[0]
                        mx.popleft()
                    else:
                        fin = mn[0]
                        mn.popleft()
                else:
                   # print(ind,z)
                    ans += z - 1
                    break
        return ans

        