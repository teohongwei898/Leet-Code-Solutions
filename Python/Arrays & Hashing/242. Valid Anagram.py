class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            countS ={}
            countT = {}
            for i in s:
                countS[i] = 1 + countS.get(i, 0) 
                #Cannot do 1+ countS[i], in case there is no key with that char. 0 is the default value
            for j in t:
                countT[j] = 1+ countT.get(j, 0)
            for k in countS:
                if countS[k] != countT.get(k,0):
                    return False
            return True
