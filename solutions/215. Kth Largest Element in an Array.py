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
        L, M = len(right), len(mid)
​
        if k <= L:
            return self.findKthLargest(right, k)
        elif k > L + M:
            return self.findKthLargest(left, k - L - M)
        else:
            return mid[0]
