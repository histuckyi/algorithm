class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vertical_tree_dict = dict()
        root.val = (0, 0, root.val)
        tree_node_list = [root]
        count = 0
        while len(tree_node_list) != 0:
            count += 1
            cur_node = tree_node_list.pop(0)
            cur_row, cur_col, cur_value = cur_node.val
            if cur_node.left is not None:
                cur_node.left.val = (cur_row + 1, cur_col - 1, cur_node.left.val)
                tree_node_list.append(cur_node.left)

            if cur_node.right is not None:
                cur_node.right.val = (cur_row + 1, cur_col + 1, cur_node.right.val)
                tree_node_list.append(cur_node.right)

            if cur_col in vertical_tree_dict:
                vertical_tree_dict[cur_col].append(cur_node.val)
            else:
                vertical_tree_dict[cur_col] = [cur_node.val]

        result = []

        # key는 같은 col
        for key in sorted(vertical_tree_dict.keys()):

            mini_result_dict = dict()
            mini_result_list = []

            for value in vertical_tree_dict[key]:
                if value[0] in mini_result_dict:
                    # 같은 row인 경우를 모은다
                    mini_result_dict[value[0]].append(value[2])
                    # 오름 차순으로 정렬시킨다
                    mini_result_dict[value[0]] = sorted(mini_result_dict[value[0]])
                else:
                    mini_result_dict[value[0]] = [value[2]]

                # position이 작은 순서대로 다시 조합한다
            for k in sorted(mini_result_dict.keys()):
                mini_result_list = mini_result_list + mini_result_dict[k]

            result.append(mini_result_list)

        return result