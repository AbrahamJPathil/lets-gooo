class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVal = 0
        start = 0
        end = len(heights) - 1
        while(start < end):
            currHt = (end-start)*min(heights[start],heights[end])
            maxVal = max(maxVal,currHt)
            if heights[start] > heights[end]:
                end -= 1
            elif heights[end] > heights[start]:
                start += 1
            else:
                end -= 1
        
        return maxVal
        
        