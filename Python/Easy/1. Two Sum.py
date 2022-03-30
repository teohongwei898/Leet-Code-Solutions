#Brute Force

class Solution:
    def BruteForcetwoSum(self, nums: List[int], target: int) -> List[int]:        
        for i in range(len(nums)):    
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
              
#Time: O(n), Size: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Initialize Hashmap
      #Check if Target - value is in hashmap, if not, add index to hashmap
      #In the first iteration, hashmap is empty. Hence 100% will map to hashmap first.
      #End result, may not even need to map everything to hashmap since the results may be in the middle of the hashmap.
      #Enumerate tracks index and value in array.
      prevMap = {} #Value:Index!!!
      for i,n in enmuerate(nums):
        diff = target - n           
        if diff in prevMap:
          return (prevMap[diff],i)   #So since the keys are the values, and the 'stored values' are the indexes, I can return and find the index where the value was placed at.
        prevMap[n] = i  #So to store, I take the value of the list as the key, and the 'stored value' to be where it was found in the list aka index number in list.
                     
              
