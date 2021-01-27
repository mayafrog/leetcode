class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    
        minWindowSize = len(nums)+1
        currentWindowSum = 0
        windowStart = 0
​
        for windowEnd in range(len(nums)):
            currentWindowSum += nums[windowEnd]
​
            while currentWindowSum >= s:
                minWindowSize = min(minWindowSize, windowEnd-windowStart + 1)
                currentWindowSum -= nums[windowStart]
                windowStart += 1
​
        return minWindowSize if minWindowSize <= len(nums) else 0
