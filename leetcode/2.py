"""
LeetCode 2. Add Two Numbers
blog : https://daimhada.tistory.com/116
problem : https://leetcode.com/problems/add-two-numbers/submissions/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Runtime : faster than 39.31% of Python3
    Memory Usage : 13.5 MB, less than 5.21% of Python3
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        curn = l1
        num = 1
        first_number = 0
        while curn:
            first_number += curn.val * num
            curn = curn.next
            num *= 10

        curn = l2
        num = 1
        secound_number = 0

        while curn:
            secound_number += curn.val * num
            curn = curn.next
            num *= 10

        number = first_number + secound_number

        head = None
        for i in reversed(str(number)):
            print(i)
            if not head:
                head = ListNode(int(i))
                curn = head
            else:
                curn.next = ListNode(int(i))
                curn = curn.next
        return head