class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return len(nums)
        nums.sort()
        count = 0
        i = 0
        while i < len(nums):
            r = i + 1
            iteration = 1
            while(r < len(nums) and nums[r] == nums[i] + iteration):
                iteration+=1
                r += 1
            
            currWindow = r - i + 1;
            if(currWindow > count):
                count = currWindow
            i = r
        
        return count
