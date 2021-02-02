class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
​
        for c in s:
            if c in hash:
                hash.remove(c)
            else:
                hash.add(c)
​
        if len(hash) > 0:
            return (len(s) - len(hash) + 1)
        else:
            return (len(s))
