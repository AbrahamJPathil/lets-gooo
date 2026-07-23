class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            letterCount = [0]*26
            for c in word:
                letterCount[ord(c)-ord('a')] += 1
            res[tuple(letterCount)].append(word)
        
        return list(res.values())
        