class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurr = maxGlobal = nums[0]
        for i in range(1, len(nums)):
                  maxCurr = max(nums[i],nums[i]+maxCurr)
                  if (maxCurr > maxGlobal):
                        maxGlobal = maxCurr
        return maxGlobal
                
