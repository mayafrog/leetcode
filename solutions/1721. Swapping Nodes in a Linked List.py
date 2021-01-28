# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        node = head
​
        while node:
            length += 1
            node = node.next
​
        if k == length - k + 1:
            return head
​
        node = head
        counter = 0
        prev = head
        ahead = head
​
        while node:
            counter += 1
            if counter == k:
                prev = node
            elif counter == length - k + 1:
                ahead = node
            node = node.next
​
        prev.val, ahead.val = ahead.val, prev.val
​
        return head
