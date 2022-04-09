class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =defaultdict(list)  #Count of each Char:words
        
        for s in strs:
            count = [0] * 26   #[0] * x creates a list with x elements.
            for c in s:  #a is index 0, z is index 25
                count[ord(c)-ord("a")] +=1 
            res[tuple(count)].append(s)
        return res.values()
