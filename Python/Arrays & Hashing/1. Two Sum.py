
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #Value:Index
        for i, n in enumerate(nums):   #i is index, n is value
            diff = target - n           #target - value to find diff.
            if diff in prevMap:         #if diff in hashmap, find index, else put value in hashmap with index
                return [prevMap[diff], i]
            prevMap[n] = i
