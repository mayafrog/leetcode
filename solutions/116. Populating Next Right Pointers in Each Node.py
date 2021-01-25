"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
​
        current_node = root
        next_node = root.left
​
        while current_node.left:
            current_node.left.next = current_node.right
​
            if current_node.next:
                current_node.right.next = current_node.next.left
                current_node = current_node.next
​
            else:
                current_node = next_node
                next_node = current_node.left
​
        return root
​
