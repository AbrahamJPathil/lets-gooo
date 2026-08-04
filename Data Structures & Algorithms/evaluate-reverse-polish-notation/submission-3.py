from collections import deque
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        chars = deque()
        for s in tokens:
            if(s.isnumeric()):
                chars.append(int(s))
            else:
                nums = []
                nums.append(chars[-1])
                chars.pop()
                nums.append(chars[-1])
                if(s == '*'):
                    chars.append((nums[1])*(nums[0]))
                elif(s == '+'):
                    chars.append(nums[1]+nums[0])
                elif(s == '-'):
                    chars.append(nums[1]-nums[0])
                else:
                    divRes = nums[1]/nums[0]
                    chars.append(math.floor(divRes))
        return chars[-1] 
        
        
        