class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        odd = []
        even = []
​
        for i in range (0, len(A)):
            if (A[i] % 2) == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        
        result = even + odd
        return result
