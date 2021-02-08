# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        height = 0
        res = [root.val]
​
        while queue:
            temp_queue = []
            temp_res = []
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                    temp_res.append(node.left.val)
                if node.right:
                    temp_queue.append(node.right)
                    temp_res.append(node.right.val)
            if temp_res:
                res.append(max(temp_res))
            queue = temp_queue
        
        return res
