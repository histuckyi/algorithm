import sys
input = sys.stdin.readline


def dfs(type, pos, board, visited):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    position_list = []
    position_list.append(pos)
    visited[pos[0]][pos[1]] = 1 # check visited position
    while position_list:
        r, c = position_list.pop()
        current_color = board[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr and 0 <= nc and nr < n and nc < n and not visited[nr][nc]:
                next_color = board[nr][nc]

                # basic condition
                if current_color == next_color:
                    visited[nr][nc] = 1
                    position_list.append((nr, nc))
                    continue

                # only condition for unnormal
                if type == 1 and (current_color == 'R' or current_color == "G") \
                            and (next_color == "R" or next_color == "G"):
                    visited[nr][nc] = 1
                    position_list.append((nr, nc))

def solve(n, board):
    visited_0 = [[0]*n for j in range(n)]
    visited_1 = [[0]*n for j in range(n)]
    count_0 = 0
    count_1 = 0
    for r in range(n):
        for c in range(n):
            if not visited_1[r][c]:
                dfs(1, (r,c), board, visited_1)
                count_1 += 1
            if not visited_0[r][c]:
                dfs(0, (r,c), board, visited_0)
                count_0 += 1
    print("{0} {1}".format(count_0, count_1))

if __name__ == "__main__":
    n = int(input().strip())
    board = []
    for i in range(n):
        board.append(list(input().strip()))
    solve(n, board)
