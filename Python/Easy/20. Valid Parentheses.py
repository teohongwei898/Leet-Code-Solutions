class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<2:
            return False
        for i in range(len(s)-1):
            if s[i] == ("(" or "{" or "["):
                stack.append(s[i])
            if s[i] == ")":
                if not stack or stack.pop() != "(":                 #If stack empty or the one that is being popped off does not match, return False
                    return False
                
            if s[i] == "]":
                if not stack or stack.pop() != "[":
                    return False
                
            if s[i] == "}":
                if not stack == True or stack.pop() != "{":
                    return False
                
        
        return True
            
            
                
        
