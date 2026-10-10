class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        for i in range(len(nums1)):
            nums1[i] = abs(nums1[i]-nums2[i])
        nums1.sort(reverse = True)
        i = 0
        k1+= k2
        imp,pos = nums1[0], -1
        while imp>pos:
            mid = (pos+imp+1)//2
            z = sum(max(0,val-mid) for val in nums1)
            if z>k1:
                pos = mid
            else:
                imp = mid - 1
        pos += 1
        for i in range(len(nums1)):
            k1 -= max(0, nums1[i] - pos)
            nums1[i] = min(pos,nums1[i])
        if nums1[0]>0:
            for i in range(k1):nums1[i] -= 1

        return sum(v*v for v in nums1)



        