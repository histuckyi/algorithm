"""
LeetCode : 938. Range Sum of BST
blog : https://daimhada.tistory.com/184
problem : https://leetcode.com/problems/range-sum-of-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = TreeNode(data)
    else:
        if (data <= node.val):
            node.left = _insert_node_into_binarysearchtree(node.left, data)
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data)
    return node



class Solution:
    def checkChildBST(self, root, result, l, r):

        # if leaf node, recursion must be closed
        if root == None:
            return result

        if root.val <= l:
            if root.val == l:
                result += root.val
            result = self.checkChildBST(root.right, result, l, r)

        if r <= root.val:
            if r == root.val:
                result += root.val
            result = self.checkChildBST(root.left, result, l, r)

        if l < root.val < r:
            result = self.checkChildBST(root.left, result + root.val, l, r)
            result = self.checkChildBST(root.right, result, l, r)

        # Returns the result of the tree of child
        return result


    def rangeSumBST(self, root, L: int, R: int) -> int:
        return self.checkChildBST(root, 0, L, R)


if __name__ == "__main__":
    root = _insert_node_into_binarysearchtree(None, 10)
    node = _insert_node_into_binarysearchtree(root, 5)
    node = _insert_node_into_binarysearchtree(root, 15)
    node = _insert_node_into_binarysearchtree(root, 3)
    node = _insert_node_into_binarysearchtree(root, 7)
    node = _insert_node_into_binarysearchtree(root, 18)
    node = _insert_node_into_binarysearchtree(root, 1)
    node = _insert_node_into_binarysearchtree(root, 6)

    s = Solution()
    print(s.rangeSumBST(root, 7, 15))
    print(s.rangeSumBST(root, 6, 10))