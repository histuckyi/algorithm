"""
1008. Construct Binary Search Tree from Preorder Traversal
problem: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/submissions/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def bstFromPreorder(preorder):
        root = TreeNode()
        root.val = preorder.pop(0)

        while len(preorder) != 0:
            value = preorder.pop(0)
            node = root
            is_left = False
            while node:
                is_left = False
                prev_node = node
                if value < node.val:
                    is_left = True
                    node = node.left
                else:
                    node = node.right

            if is_left:
                prev_node.left = TreeNode(value)
            else:
                prev_node.right = TreeNode(value)
        return root


if __name__ == "__main__":
    s = Solution()
    s.bstFromPreorder([8,5,1,7,10,12])