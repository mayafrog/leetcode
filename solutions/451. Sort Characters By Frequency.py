class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        print(count)
​
        count = count.most_common()
​
        res = []
​
        for i, j in count:
            res += ([i] * j)
​
        return(res)
​
