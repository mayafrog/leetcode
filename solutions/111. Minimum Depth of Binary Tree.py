# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
​
        queue = [root]
        res = []
        level = 0
​
        while queue:
            temp = []
            level += 1
            for node in queue:
                if not node.left and not node.right:
                    if res:
                        if level > min(res):
                            queue = []
                            break
                    res.append(level)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        
        return min(res)
