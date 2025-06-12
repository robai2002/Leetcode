class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        m = dict()
        n = 1
        for i,v in enumerate(sorted(set(nums)),start = 1):
            m[v] = i
            n += 1
        st = [0]*n
        
        def query(x: int) ->int:
            val = 0
            while(x):
                val += st[x]
                x -= x&(-x)
            return val

        def update(x: int) ->None:
            while x<n:
                st[x] += 1
                x += x&(-x)
        

        ans = [0]*len(nums)
        for i in reversed(range(len(nums))):
            ans[i] = query(m[nums[i]]-1)
            update(m[nums[i]])

            
        return ans