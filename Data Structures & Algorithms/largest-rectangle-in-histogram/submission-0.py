from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        finalHt = deque()
        maxArea = 0 
        for i,h in enumerate(heights):  #[i,h]
            currMax = 0
            while(finalHt and h < finalHt[-1][1]):
                maxArea = max(maxArea,(finalHt[-1][1]*(i-finalHt[-1][0])))
                finalHt.pop()
            
            finalHt.append([i,h])

        return maxArea