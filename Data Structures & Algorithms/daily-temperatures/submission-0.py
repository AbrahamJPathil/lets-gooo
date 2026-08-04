class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            currTmp = temperatures[i]
            dayCount = 0
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > currTmp:
                    dayCount = j - i
                    break
            
            res.append(dayCount)
        return res
        