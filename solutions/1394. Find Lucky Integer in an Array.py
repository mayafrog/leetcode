class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = [0] * 500
        largest = 0
​
        for i in arr:
            counter[i-1] += 1
​
        for i in range(0, len(counter)):
            if counter[i] == i+1 and counter[i] > largest:
                largest = counter[i]
        
        if largest != 0:
            return largest
        else:
            return -1
