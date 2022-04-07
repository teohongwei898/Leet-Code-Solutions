class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    
    #Want Ologn

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r= len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return m
        return -1
    
