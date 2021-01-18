class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        leaving = list()
        for i in paths:
            leaving.append(i[0])
​
        for i in paths:
            if i[1] in leaving:
                continue
            else:
                return i[1]
​
