class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''
        for word in strs:
            n = len(word)
            st += str(n)+'#'
            st += word
        
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j]!='#'):
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            res.append(word)
            i = j + length + 1

        return res


