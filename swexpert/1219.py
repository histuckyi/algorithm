"""
SW Expert Academy 1219. 길찾기
blog : https://daimhada.tistory.com/86
"""

def gen():
    table = dict()
    t, e = map(int, input().strip().split())

    start = None
    for v in map(int, input().strip().split()):
        if start is None:
            start = v
        else:
            if str(start) in table:
                table[str(start)].append(str(v))
            else:
                table[str(start)] = [str(v)]
            start = None
    yield t, table


def solve(table):
    visited = [False] * 100
    next_pos = table['0']
    while next_pos:
        pos = next_pos.pop()

        # Check visited city
        if visited[int(pos)]:
            continue
        else:
            # If not visited, check linked cities
            add_next_pos = []
            if pos in table:
                add_next_pos = table[pos]
            # Check if '99' city is in next city's List
            if '99' in add_next_pos:
                return 1
            
            next_pos.extend(add_next_pos)
    return 0


if __name__ == "__main__":
    for i in range(10):
        for t, table in gen():
            print("#{0} {1}".format(t, solve(table)))
