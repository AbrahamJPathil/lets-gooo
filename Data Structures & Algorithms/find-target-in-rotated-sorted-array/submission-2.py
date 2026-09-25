class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = int((l + r)/2)
            curr = nums[mid]
            if(curr == target):
                return mid
            elif(curr < target):
                l = mid + 1
                continue
            else:
                if(nums[0] < target):
                    r = mid - 1
                    continue
                else:
                    l = mid + 1
                    continue
        return -1
        
