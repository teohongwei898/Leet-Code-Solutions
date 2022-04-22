class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            #check left/right sorted portion
            if nums[m] >= nums[0]:
                if target > nums[m] or target < nums[0]:
                    l = m + 1
                else:
                    r = m - 1
            #right sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m + 1
        return -1
