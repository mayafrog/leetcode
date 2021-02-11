class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
​
        arr = [True] * n
        arr[0] = False
        arr[1] = False
​
        for i in range (2, n):
            for j in range (i*i, n, i):
                arr[j] = False
        
        return sum(arr)
