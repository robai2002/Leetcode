class Solution:
        def findGoodIntegers(self, n: int) -> list[int]:

            cubes = [x * x * x for x in range(1, ceil(n**(1/3)))] 
            first, ans = set(), set()

            for i, xCubed in enumerate(cubes):                  
                for yCubed in cubes[i:]:
                    cubeSm = xCubed + yCubed
                    if cubeSm > n: break
                    
                    if cubeSm not in first:
                        first.add(cubeSm)
                    else:
                        ans.add(cubeSm)

            return sorted(ans)                                     # <-- 3)