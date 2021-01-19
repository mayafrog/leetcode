class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter_array = [0] * len(nums)
        res = []
​
        if not nums:
            return res
​
        for i in range(0, len(nums)):
            temp = nums[i] - 1
            counter_array[temp] += 1
​
        for i in range(0, len(counter_array)):
            if (counter_array[i] == 0):
                res.append(i + 1)
​
        return res
​
