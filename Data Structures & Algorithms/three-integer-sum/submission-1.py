class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
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
                    res.add(tuple([nums[i],nums[start],nums[end]]))
                    break
        
        return res
