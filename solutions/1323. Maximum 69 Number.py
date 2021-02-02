class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(x) for x in str(num)]
​
        for i in range(0, len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
​
        digits = [str(x) for x in (digits)]
        result = int("".join(digits))
​
        return(result)
