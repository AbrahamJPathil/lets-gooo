class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if(len(A) > len(B)):
            A,B=B,A
        
        halfCount = len(A+B)//2


        l = 0
        r = len(A) - 1
        while(True):
            i = (l+r)//2
            if i >= 0:
                Aleft = A[i]
            else: 
                Aleft = float("-inf")
            
            if i+1<len(A):
                Aright = A[i+1] 
            else:
                Aright = float("inf")

            oh = halfCount - i - 2
            if(oh >= 0):
                Bleft = B[oh]
            else:
                Bleft = float("-inf")
            
            if oh + 1 < len(B):
                Bright =  B[oh + 1] 
            else:
                Bright = float("inf")

            #check for valid half
            if(Aleft <= Bright and Bleft <= Aright):
                if len(A+B) % 2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright))/2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i+1
        




        