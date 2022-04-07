class Solution:
    def isValid(self, s: str) -> bool:
        
#Cannot start with closing parentheses
#Remove closing with opening, if empty means okay because close all


        stack = []
        closeToOpen = {")":"(", "]":"[","}":"{"}
        for c in s:
            if c in closeToOpen:   #if closing bracket,
                if stack and stack[-1] == closeToOpen[c]:   
                    stack.pop()
                else:
                    return False                  #if stack is empty or close bracket no match, false. else pop and check next bracket
            else:
                stack.append(c)   #if is opening bracket, then just append to stack
                
        if not stack:           #at end, stack empty means all good. else fail.
            return True
        else:
            return False
        
                
                





























        
