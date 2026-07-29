class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        collection = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num,no_occ in freq.items():
            collection[no_occ].append(num)
        

        res = []
        for i in range(len(nums),0,-1):
            current = collection[i]
            for n in current:
                if(len(res) == k):
                    break
                res.append(n)
        
        return res


        