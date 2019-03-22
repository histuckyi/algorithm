from itertools import combinations

def solve(n, m, board):
    chicken_list = []
    home_list = []
    distance_dict = {}

    # check chicken, home
    for i in range(n):
        for j in range(n):
            v = board[i][j]
            if v == 2:
                chicken_list.append((i,j))
            elif v == 1:
                home_list.append((i,j))

    # the most shortest chicken distance (append chicken_list's index)
    like_chicken_list = []

    min_total = 0
    # All chicken distance from home
    for home in home_list:
        r1,c1 = home
        key = str(home)
        distances = []
        best_index = -1
        best_distance = 9999999
        for idx, chicken in enumerate(chicken_list):
            r2, c2 = chicken
            distance = abs(r1 - r2) + abs(c1 - c2)
            distances.append(distance)
            if distance < best_distance:
                best_distance = distance
                best_index = idx
        min_total += distances[best_index] # the shortest chicken's distance
        like_chicken_list.append(best_index)
        distance_dict[key] = distances # add distance at each chicken restaurant from home

    result = 99999999
    # selection : closed chicken restaurant
    for selection in combinations(range(0,len(chicken_list)), len(chicken_list) - m):
        temp_min_total = min_total

        for idx, like in enumerate(like_chicken_list):
        # Find home that used the closed chicken restaurant
        # Get the other minimum chicken's distance.
         if like in selection:
            home = home_list[idx]
            # find other chicken restaurent
            min_v = 99999999

            # reuse total distance that already have saved
            distances = distance_dict[str(home)]
            for i, distance in enumerate(distances):
                # previous chicken restaurent
                if i  == like:
                    temp_min_total -= distance
                    # Subtract previous chicken's distance
                elif i not in selection:
                    if min_v > distance:
                        min_v = distance
            # recalculate value
            temp_min_total += min_v
        if temp_min_total < result:
            result = temp_min_total
    return result


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    board = []
    for i in range(n):
        line = list(map(int, input().strip().split()))
        board.append(line)
    print(solve(n, m, board))