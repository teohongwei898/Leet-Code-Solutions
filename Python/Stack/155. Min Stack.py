class MinStack:

    def __init__(self):
        self.stack = []                 #create 2 stacks at once, one for normal, one for min
        self.minStack =[]
        
      
    def push(self, val: int) -> None:   #idea is to append both stacks at the same time, min should always contain the min value, while the other one will proceed as normal
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])  # -1 to get the top value of stack
            self.minStack.append(val)
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()    #remember to pop both stacks at once
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]   


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
