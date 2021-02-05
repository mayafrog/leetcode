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
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
​
        res = []
        level = 0
​
        def dfs(root, level):
            if not root:
                return
​
            else:
                if not root.children:
                    res.append(level)
​
                else:
                    for child in root.children:
                        dfs(child, level+1)
​
        dfs(root, 1)
        return max(res)
​
