class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} #Hashmap
        #If value of first index < value of second index, first index is negative
        #If value of first index > value of second index, +ve
        #Reference to hashmap for values
        result = 0
        for i in range(len(s)):
            if  (i+1 < len(s) and roman[s[i]]<roman[s[i+1]]):  #to take into account of last value
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result
      
      
      #So for the last letter, since i+1>len(s), will just add.
