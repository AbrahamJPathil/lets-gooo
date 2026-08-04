from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        currTemps = deque()
        for i,t in enumerate(temperatures):
            while (currTemps and currTemps[-1][0] < t):
                smallTmp, smallInd = currTemps.pop()
                res[smallInd] = i-smallInd
            currTemps.append([t,i])
        
        return res
        
        