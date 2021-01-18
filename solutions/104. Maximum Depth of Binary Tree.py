# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
​
        Lcounter = self.maxDepth(root.left)
        Rcounter = self.maxDepth(root.right)
​
        if (Lcounter > Rcounter):
            return Lcounter + 1
        else:
            return Rcounter + 1
​
