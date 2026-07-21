import heapq
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = collections.defaultdict(int)
        for c in s:
            arr[c]+=1
        
        arr1 = collections.defaultdict(int)
        for c in t:
            arr1[c]+=1

        if(arr == arr1):
            return True
        else:
            return False      
        
        