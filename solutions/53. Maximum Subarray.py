class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        maximum_sum = nums[0]
​
        for i in nums[1:]:
            current_sum = max(current_sum + i, i)
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum
