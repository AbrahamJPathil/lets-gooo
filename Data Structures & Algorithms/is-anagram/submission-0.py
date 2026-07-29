import heapq
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        for c in s:
            heapq.heappush(arr,c)
        
        isAna = True
        for c in t:
            if c not in arr:
                isAna = False
                break
        
        return isAna
        