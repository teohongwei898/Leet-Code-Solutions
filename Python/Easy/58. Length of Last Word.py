class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1 
        
        
     #Remove any potential whitespace behind last word
    
        while s[i] == " ":
            i -= 1
          
   #Start from last index of last word. So if not a blank space and not at the first index, length+ 1. Once reach blank space or first index just return length       
          
        while i>=0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length
        
