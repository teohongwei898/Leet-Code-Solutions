class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap ={} #Value:Index
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff]+1,i+1]
            hashMap[n] = i
            
            
            
           #or
        
 class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R =0, len(numbers)-1
        while L<R:
            if numbers[L]+numbers[R] > target:
                R-=1
            elif numbers[L]+numbers[R] < target:
                L+=1
            else:
                return [L+1, R+1]
