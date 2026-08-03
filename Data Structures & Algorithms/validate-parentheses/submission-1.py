from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        coll = deque()
        for c in s:
            if(c == '('):
                coll.append(')')
            elif(c == '{'):
                coll.append('}')
            elif(c == '['):
                coll.append(']')
            
            else:
                lastEle = coll[-1]
                if(lastEle != c):
                    return False
                else:
                    coll.pop()
        
        return True
        
