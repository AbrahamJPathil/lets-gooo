class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        

        buckets = [[]for _ in range(len(nums)+1)]
        for n in freq:
            buckets[freq[n]].append(n)
        
        res = []
        for i in range(len(buckets)-1,-1,-1):
            
            
            curr = buckets[i]
            if(len(curr) > 0):
                for n in curr:
                    if(len(res) == k):
                        break
                    res.append(n)
        
        return res
                    

        