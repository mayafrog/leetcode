class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in (strs):
            # print ("iteration:", i)
            key = tuple(sorted(i))
            # print ("key:", key)
            dict[key] = dict.get(key, []) + [i]
            # print ("dict:", dict)
            # print ("\n")
        return (list(dict.values()))
