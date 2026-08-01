class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        coll = {}
        for i,n in enumerate(numbers):
            req = target - n
            if n in coll:
                return [coll[n],i+1]
        
            coll[req] = i+1
        
        return []