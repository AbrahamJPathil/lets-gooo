class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if(i > 0 and n == nums[i-1]):
                continue
            coll = {}
            start = i + 1
            end = len(nums) - 1
            req = -1*n
            while(start < end):
                currSum = nums[start] + nums[end]
                if(currSum > req):
                    end -= 1
                elif(currSum < req):
                    start += 1
                else:
                    res.append([nums[i],nums[start],nums[end]])
                    start += 1
                    while(start < end and nums[start] == nums[start - 1]):
                        start += 1
        
        return res

        