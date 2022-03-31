class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<2:
            return False
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif ch == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif ch == "]":
                if not stack or stack.pop() != "[":
                    return False                
            elif ch == "}":
                if not stack or stack.pop() != "{":
                    return False                
        if not stack:
            return True
        else:
            return False
            
            
#First check if length is 1/0, if so, false since no perfect scenario for that
#If opening brackets, add into stack.
#If closing brackets, check if stack is empty.
#If stack empty, means no perfect = False. If got item but popping off a different symbol also wrong
#End of all, need to check that stack is empty. To take care of scenarios like "(((". Since they are all appended!
        
