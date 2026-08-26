class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numColl = set(nums)
        maxLength = 0

        for n in nums:
            if n - 1 not in nums:
                currLength = 1
                while(n+1 in numColl):
                    currLength+=1
                    n += 1
                
                maxLength = max(currLength,maxLength)
        
        return maxLength

        