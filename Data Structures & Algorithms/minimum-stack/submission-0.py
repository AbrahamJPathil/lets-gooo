from collections import deque
class MinStack:

    def __init__(self):
        self.collect = deque()
        

    def push(self, val: int) -> None:
        self.collect.append(val)

    def pop(self) -> None:
        self.collect.pop()
        

    def top(self) -> int:
        return self.collect[-1]
        

    def getMin(self) -> int:
        minVal = float('-inf')
        for n in self.collect:
            if(type(n) != int):
                continue
            else:
                if(minVal == float('-inf')):
                    minVal = n
                else:
                    minVal = min(n,minVal)
        
        return minVal
