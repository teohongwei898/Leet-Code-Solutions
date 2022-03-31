class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[x]:
                x+=1
                nums[x] = nums[i]         
        return x + 1
  
 #Remove duplicates in the list
#[1,2,3,4,4]
#Zero index will always be unique
#Scan 1st index, if same as 0 index, leave it. But different (2 v 1), hence, assign value in index 1 to index 1 -> [1,2,3,4,4] , x =1
#Scan 2nd index. If second index same as 1st index, leave. But different (3 v 2), hence assign value in index 2 to index 2 -> [1,2,3,4,4] , x=2
#Scan 3rd index. Third index different (4 v 3), assign value in third index to third index, x=3
#Scan 4th index. 4th same as 3rd. leave. -> [1,2,3,4,4] , x=3
#Req of question is to return value of duplicate, and the front part of the string must be good; behind no need care.
#Hence, return x+1 =4  since got 4 unique values.
