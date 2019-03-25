"""
백준 16235. 나무재테크
blog : https://daimhada.tistory.com/114
problem : https://www.acmicpc.net/problem/16235
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

tree_count = 0

def solve(board, nutritions, tree_dict, k):
    """
    :param board : field
    :param nutritions: given nutritions
    :param tree_dict: tree's data
    :param k: year
    :return: remained tree's count
    """
    global tree_count
    year = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    while year < k:

        # spring, summer, winter
        for i in range(n*n):
            r = i // n
            c = i % n

            nutrition = board[r][c]
            add_nutrition = 0
            trees = tree_dict[(r, c)]

            # If there is no tree planted, it will only supply nutrients.
            if not trees:
                add_nutrition += nutritions[r][c]
                add_nutrition += nutrition
                board[r][c] = add_nutrition
                continue

            cnt = len(trees)
            temp_trees = []
            # spring & summer
            while 0 < cnt:
                tree = trees.pop()
                checked = nutrition - tree
                # check if nutrients remain
                if 0 <= checked:
                    nutrition -= tree
                    temp_trees.append(tree + 1)
                else:
                    # 유효하지 않으므로, 나무 죽이기
                    add_nutrition += (tree // 2)
                    tree_count -= 1
                cnt -= 1
            # 성장한 나무들을 기존 배열에 추가해준다
            trees.extend(temp_trees)

            if 1 < len(trees):
                trees.sort(reverse= True)

            # winter
            add_nutrition += nutritions[r][c]
            add_nutrition += nutrition
            board[r][c] = add_nutrition

        # autumn
        for key, value in tree_dict.items():
            spread_tree_count = 0
            if len(value) == 0:
                continue

            for i in value:
                # if the oldest tree is less than 5, break
                if i < 5:
                    break
                if i % 5 == 0:
                    spread_tree_count += 1

            if spread_tree_count > 0:
                r, c = key
            for d in range(8):
                temp_r = r + dr[d]
                temp_c = c + dc[d]
                if 0 <= temp_r < n and 0 <= temp_c < n:
                    # breed Tree
                    tree_count += spread_tree_count
                    tree_dict[(temp_r, temp_c)].extend([1]*spread_tree_count)
        # add year
        year += 1
    print(tree_count)
    return tree_count

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    nutritions = []
    board = [[5]*n for _ in range(n)]

    for i in range(n):
        nutritions.append(list(map(int, input().split())))

    # Store the trees(age) in dict, key is position
    tree_dict = defaultdict(lambda :[])
    for t in range(m):
        r, c, old = map(int, input().strip().split())
        tree_dict[(r-1,c-1)].append(old)
        tree_count += 1
    solve(board, nutritions, tree_dict, k)
