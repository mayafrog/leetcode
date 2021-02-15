class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if (len(nums) <= 1):
            return nums
        
        pivot = random.choice(nums)
​
        left = [i for i in nums if i < pivot]
        middle = [i for i in nums if i == pivot]
        right = [i for i in nums if i > pivot]
​
        return self.sortArray(left) + middle + self.sortArray(right)
