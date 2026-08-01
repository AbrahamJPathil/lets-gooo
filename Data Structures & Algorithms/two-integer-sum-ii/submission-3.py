class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while(start < end):
            s = numbers[start] + numbers[end]
            while(start < len(numbers) and s < target):
                start += 1
                s = numbers[start] + numbers[end]
            while(end >= 0 and s > target):
                end -= 1
                s = numbers[start] + numbers[end]
            if(start == len(numbers) or end == -1):
                return []
            if(s == target):
                return [start+1,end+1]
        return []