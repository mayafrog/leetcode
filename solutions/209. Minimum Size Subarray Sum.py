class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    
        window = len(nums)+1
        sum = 0
        l = 0
​
        for r in range(0,len(nums)):
            sum += nums[r]
​
            while sum >= s:
                window = min(window, r-l + 1)
                sum -= nums[l]
                l += 1
​
        return window if window <= len(nums) else 0
