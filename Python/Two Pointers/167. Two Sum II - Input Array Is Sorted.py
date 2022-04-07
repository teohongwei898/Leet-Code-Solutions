class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap ={} #Value:Index
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff]+1,i+1]
            hashMap[n] = i
