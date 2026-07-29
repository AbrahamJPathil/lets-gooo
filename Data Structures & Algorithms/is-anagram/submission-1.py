import heapq
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = collections.defaultdict(int)
        for c in s:
            arr[c]+=1
        
        arr1 = collections.defaultdict(int)
        for c in t:
            arr1[c]+=1

        isAna = True
        for k in arr:
            if(arr[k]!=arr1[k]):
                isAna = False
                break

        return isAna        
        
        