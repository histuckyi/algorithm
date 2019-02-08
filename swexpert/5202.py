
def gens(t):
    n = int(input())
    timetable = []
    for i in range(n):
        time = tuple(map(int, input().strip().split(' ')))
        timetable.append(time)
    sorted_by_second = sorted(timetable, key=lambda  tup:tup[1])
    yield sorted_by_second



if __name__ == "__main__":
    t = int(input())
    for schedules in gens(t):
        pass


    """
1
5
20 23
17 20
23 24
4 14
8 18
    """