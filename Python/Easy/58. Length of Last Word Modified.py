#LENGTH OF LONGEST WORD IN STRING

class Solution:
    def lengthOfLongestWord(self, s: str) -> int:
        length = 0
        i = 0
        maxCurr =0
        while i < len(s):
            if s[i]==" ":
                i += 1
                if maxCurr > length:
                    length = maxCurr
                maxCurr = 0
            
            else:
                maxCurr +=1
                i+=1
         
        if maxCurr > length:
                    return maxCurr
        else:
            return length
                     
                
                
        
