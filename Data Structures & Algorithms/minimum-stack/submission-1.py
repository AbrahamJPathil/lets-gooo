from collections import deque
class MinStack:

    def __init__(self):
        self.nStack = deque()
        self.minStack = deque()
        

    def push(self, val: int) -> None:
        if(len(self.minStack) == 0):
            self.minStack.append(val)
        else:
            self.minStack.append(min(val,self.minStack[-1]))
        
        self.nStack.append(val)
    
        

    def pop(self) -> None:
        self.nStack.pop()
        self.minStack.pop()
        

    def top(self) -> int:

        return self.nStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
