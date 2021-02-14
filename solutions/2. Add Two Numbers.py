# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1 = []
        current = l1
        while current:
            arr1.insert(0, current.val)
            current = current.next
​
        arr2 = []
        current = l2
        while current:
            arr2.insert(0, current.val)
            current = current.next
​
        str1 = [str(i) for i in arr1]
        val1 = int("".join(str1))
​
        str2 = [str(i) for i in arr2]
        val2 = int("".join(str2))
​
        result = str(val1+val2)
​
        reversed = result[::-1]
        res = ListNode(reversed[0])
        temp = res
        head = res
​
        for i in range(1, len(reversed)):
            temp.next = ListNode(reversed[i])
            res = temp
            temp = res.next
​
        return head
​
