class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        print ("pivot:", pivot)
​
        right =  [x for x in nums if x > pivot]
        print ("right:", right)
        mid  =  [x for x in nums if x == pivot]
        print ("mid:", mid)
        left = [x for x in nums if x < pivot]
        print ("left:", left)
​
        R, M = len(right), len(mid)
​
        if k <= R:
            return self.findKthLargest(right, k)
        elif k > R + M:
            return self.findKthLargest(left, k - R - M)
        else:
            return mid[0]
