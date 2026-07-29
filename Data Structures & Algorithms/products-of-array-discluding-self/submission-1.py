class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        for i in range(len(nums)):
            if(i==0):
                pre[i] = nums[i]
            else:
                pre[i] = nums[i]*pre[i-1]
        
        for j in range(len(nums)-1,-1,-1):
            if(j == len(nums)-1):
                post[j] = nums[j]
            else:
                post[j] = nums[j] * post[j+1]
        
        res = [0]*len(nums)
        for i in range(len(nums)):
            if(i == 0):
                res[i] = post[i+1]
            elif(i == len(nums)-1):
                res[i] = pre[i-1]
            else:
                res[i] = pre[i-1] * post[i+1]
        
        return res
        