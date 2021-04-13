class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        maximum_sum = nums[0]
​
        for number in nums[1:]:
            current_sum = max(number, current_sum + number)
            maximum_sum = max(current_sum, maximum_sum)
        
        return maximum_sum
