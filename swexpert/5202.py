"""
SW Expert Academy 5202. 화물도크(D3)
blog : https://daimhada.tistory.com/32

* To allow as many lorries as possible, the lorries that terminate the work in the shortest time will first deliver the cargo
"""

def gens(t):
    for i in range(t):
        n = int(input())
        timetable = []
        for j in range(n):
            time = tuple(map(int, input().strip().split(' ')))
            timetable.append(time)
        sorted_timetable = sorted(timetable, key=lambda  tup:tup[1])
        yield sorted_timetable

def greedy(sorted_timetable):
    truck_count = 0
    truck = sorted_timetable.pop(0)
    truck_count += 1
    flag = True
    while len(sorted_timetable) != 0 and flag:
        end_time = truck[1]
        for index, time in enumerate(sorted_timetable):
            if time[0] >= end_time:
                truck = sorted_timetable.pop(index)
                truck_count += 1
                sorted_timetable = sorted_timetable[index:]
                break
            # stop if not found until the last index
            if len(sorted_timetable) - 1 == index:
                flag = False
                break
    return truck_count


if __name__ == "__main__":
    num = 0
    t = int(input())
    for schedules in gens(t):
        num += 1
        print('#{0} {1}'.format(num, greedy(schedules)))
