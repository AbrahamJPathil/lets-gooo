class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l1,l2 = 0,0
        res = []
        while(l1 < len(nums1) and l2 < len(nums2)):
            if(nums1[l1]<nums2[l2]):
                res.append(nums1[l1])
                l1 += 1
            else:
                res.append(nums2[l2])
                l2 += 1
        
        while(l1 < len(nums1)):
            res.append(nums1[l1])
            l1 += 1
        
        while(l2 < len(nums2)):
            res.append(nums2[l2])
            l2 += 1
        
        if(len(res)%2):
            return res[len(res)//2]
        
        else:
            return (res[len(res)//2]+res[len(res)//2-1])/2

        