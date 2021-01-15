"""
1302. Deepest Leaves Sum
problem: https://leetcode.com/problems/deepest-leaves-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def deepestLeavesSum(self, root):
        result = []
        node_list = [(0, root)]
        # 모든 트리의 node 순회
        while node_list:
            level, cnode = node_list.pop(0)

            if len(result) - 1 < level:
                result.append(cnode.val)
            else:
                result[level] += cnode.val

            if cnode.left:
                node_list.append((level+1, cnode.left))

            if cnode.right:
                node_list.append((level+1, cnode.right))

        return result[-1]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    lnode = root.left
    rnode = root.right
    lnode.left = TreeNode(4)
    lnode.right = TreeNode(5)
    rnode.right = TreeNode(6)
    lnode.left.left = TreeNode(7)
    rnode.right.right = TreeNode(8)

    s = Solution()
    print(s.deepestLeavesSum(root))
