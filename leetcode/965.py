"""
LeetCode : 965. Univalued Binary Tree
blog : https://daimhada.tistory.com/185
problem : https://leetcode.com/problems/univalued-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# while loop
class Solution:
    def isUnivalTree(self, root) -> bool:
        node_list = [root]
        while node_list:
            cnode = node_list.pop()
            if cnode.val == root.val:
                if cnode.left: node_list.append(cnode.left)
                if cnode.right: node_list.append(cnode.right)
            else:
                return False
        return True


# Recursion
class Solution:
    def isUnivalTree(self, root) -> bool:
        if root:
            if root.left:
                if root.val != root.left.val:
                    return False

            if root.right:
                if root.val != root.right.val:
                    return False
        else:
            return True
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    lnode = root.left
    rnode = root.right
    lnode.left = TreeNode(1)
    lnode.right = TreeNode(1)
    rnode.right = TreeNode(1)


    s = Solution()
    print(s.isUnivalTree(root))

