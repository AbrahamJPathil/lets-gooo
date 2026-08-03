from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False
        coll = deque()
        for c in s:
            if(c == '('):
                coll.append(')')
            elif(c == '{'):
                coll.append('}')
            elif(c == '['):
                coll.append(']')
            
            else:
                if(len(coll) == 0):
                    return False #started with end logic
                lastEle = coll[-1]
                if(lastEle != c):
                    return False
                else:
                    coll.pop()
        
        return True
        