"""
LeetCode 21. Merge Two sorted Lists
blog : https://daimhada.tistory.com/157
problem : https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        start = None
        while l1 and l2:
            next = None
            l1_v, l2_v  = l1.val, l2.val

            if l1_v <= l2_v:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next

            if start == None:
                start = ListNode(next.val)
                head = start
            else:
                start.next = ListNode(next.val)
                start = start.next

        if l1:
            if start:
                start.next = l1
            else:
                head = l1

        if l2:
            if start:
                start.next = l2
            else:
                head = l2

        return head


def printAll(head):
    start = head
    while start:
        print(start.val)
        start = start.next


if __name__ == "__main__":
    # 1->2->4, 1->3->4
    l1_1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l1_1 = None
    l2_1 = ListNode(0)

    s = Solution()
    result = s.mergeTwoLists(l1_1, l2_1)
    printAll(result)