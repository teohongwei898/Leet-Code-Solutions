class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = len(nums)
        i = 0
        while i < (len(nums)):
            if nums[i] == val:
                del nums[i]
                x -= 1
            else:
                i+=1          
        return x
                
                
