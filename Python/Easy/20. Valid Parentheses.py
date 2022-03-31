class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<2:
            return False
        for i in range(len(s)-1):
            if s[i] == ("(" or "{" or "["):
                stack.append(s[i])
            if s[i] == ")":
                if stack.pop() != "(":
                    return False
                else:
                    stack.pop()
            if s[i] == "]":
                if stack.pop() != "[":
                    return False
                else:
                    stack.pop()
            if s[i] == "}":
                if stack.pop() != "{":
                    return False
                else:
                    stack.pop()
        
        return True
            
            
                
        
