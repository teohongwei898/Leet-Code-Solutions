class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         #Special cases
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        result = ""
        
        
        #Use first word in list as reference.
        #First letter of first word compared to first letter of other words in list
        #If same, add to result, else just return, go to next letter and repeat.
        #If length overshot also return result
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
            
