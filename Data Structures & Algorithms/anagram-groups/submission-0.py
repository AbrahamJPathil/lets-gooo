class Solution:
    def checkifAna(self,a,b):
        arr = collections.defaultdict(int)
        for c in a:
            arr[c]+=1
        
        arr1 = collections.defaultdict(int)
        for c in b:
            arr1[c]+=1

        if(arr == arr1):
            return True
        else:
            return False
       
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            col = [strs[i]]
            visited[i] = True
            for j in range(i+1,len(strs)):
                if not visited[j] and self.checkifAna(strs[i], strs[j]):
                    col.append(strs[j])
                    visited[j] = True
            res.append(col)
            
        return res