# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
​
        def dfs(root, target, path):
            path = path + [root.val]
​
            if not root.left and not root.right and sum(path) == target:
                res.append(path)
            
            if root.left:
                dfs(root.left, target, path)
            
            if root.right:
                dfs(root.right, target, path)
​
        dfs(root, targetSum, [])
​
        return res
