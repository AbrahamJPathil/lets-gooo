from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairings = []

        distinctPairings = deque()
        for i in range(len(position)):
            pairings.append([position[i],speed[i]])

        for p,s in sorted(pairings)[::-1]:
            distinctPairings.append((target-p)/s)
            if(len(distinctPairings) >= 2 and distinctPairings[-1] <= distinctPairings[-2]):
                distinctPairings.pop()
        
        return len(distinctPairings)
        
