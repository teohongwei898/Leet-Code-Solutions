class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        
        for c in s:
            if c.isalnum() :
                newStr += c.lower()
        if newStr == newStr [::-1]:  #return newStr == newStr [::-1] works too
            return True
        else:
            return False
        
