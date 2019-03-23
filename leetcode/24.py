"""
LeetCode 24. Swap Nodes in Pairs
blog : https://daimhada.tistory.com/
problem : https://leetcode.com/problems/swap-nodes-in-pairs/
"""

class ListNode:
    def __init__(self, x, nextNode):
        self.val = x
        self.next = nextNode


class Solution:
    def swapPairs(self, currentNode):
        head = currentNode.next

        prevNode = None
        while currentNode != None:
            nextNode = currentNode.next
            if prevNode != None:
                prevNode.next = currentNode.next
            currentNode.next = nextNode.next
            nextNode.next = currentNode

            prevNode = currentNode
            currentNode = currentNode.next

        return head


if __name__ == "__main__":
    node4 = ListNode(4, None)
    node3= ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()
    newHead = solution.swapPairs(node1)
    while newHead != None:
        print(newHead.val)
        newHead = newHead.next
