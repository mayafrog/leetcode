class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return (0)
        else:
            x = 0
            y = 1
            for i in range(1, n):
                z = x + y
                x = y
                y = z
            return (y)
