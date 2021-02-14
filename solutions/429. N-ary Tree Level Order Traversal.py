"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
​
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
​
        queue = [root]
        res = []
​
        while queue:
            temp = []
            temp_res = []
            for node in queue:
                temp_res.append(node.val)
                for child in node.children:
                    temp.append(child)
            queue = temp
            res.append(temp_res)
​
        return res
​
