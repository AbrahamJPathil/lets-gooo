from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        finalHt = deque()
        maxArea = 0 
        for i,h in enumerate(heights):  #[i,h]
            currIndex = i
            while(finalHt and h < finalHt[-1][1]):
                finalIndex, finalHeight = finalHt.pop()
                maxArea = max(maxArea,(finalHeight*(i-finalIndex)))
                currIndex = finalIndex #after poping, curr ht is extended backwards, so we need their index
                
            
            finalHt.append([currIndex,h])

        lIndex = len(heights)
        lIndex = len(heights)
        # Unpack the stored index and height directly from finalHt
        for index, height in finalHt:
            maxArea = max(maxArea, height * (lIndex - index))
        
        return maxArea