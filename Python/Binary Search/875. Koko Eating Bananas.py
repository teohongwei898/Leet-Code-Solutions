class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r= 1, max(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m) #math ceiling to round up
            if hours <= h:
                res = min(res,hours) #update final results 
                r = m - 1 #search left portion
            else:
                l = m + 1 #rate too small
            
        return res
                
                
    
       
