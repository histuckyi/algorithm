
"""
    (2017) KAKAO BLIND RECRUITMENT 
    [1차] 셔틀버스
    https://programmers.co.kr/learn/courses/30/lessons/17678

    solution.
    1. 대기자들이 도착하는 시간을 담은 리스트를 이른 시간 순으로 정렬한다.
    2. 이를 위해서 시간을 분단위로, 분단위를 시간으로 변경해주는 함수를 작성한다. (stringToMinutes, minutesToString)
    3. 리스트를 앞에서부터 빼내어 버스 탑승 시간에 맞춰 도착한 사람 순으로 최대 m명까지 버스를 태운다(pop(0) 시킨다)
    4. 만약 마지막 버스의 탑승 수가 꽉 차 있으면, 맨 마지막에 도착하는 사람보다 1분 먼저 도착하면 되고
        그렇지 않고 자리가 남아있을 경우에는, 버스 도착 시간에 맞춰 느긋하게 타면 된다.
    5. 4번을 알고 풀면 쉽지만, 그렇지 않을 경우에 timing을 언제로 잡느냐가 헷가리는 문제였고,
        초기 시간 리스트가 정렬되어 있지 않다는 것을 몰랐다면 뒤늦게 시간을 할애해서 풀어야 하는 문제였다. 
"""
import copy

def sortTimeTable(timetable):
    renewaltable = []
    while timetable:
        time = stringToMinutes(timetable.pop(0))
        if renewaltable:
            i = 0
            # insertion sort
            while time > renewaltable[i]:
                if i == len(renewaltable) - 1:
                    i += 1
                    break
                else:
                    i += 1
            renewaltable.insert(i, time)
        else:
            renewaltable.append(time)
    return renewaltable
                

def solution(n, t, m, _timetable):
    currentTime = 540 # 9:00
    maxMinute = 540 + (n -1) * t # 9:00 + &
    timetable = sortTimeTable(_timetable)
    answer = None
    currentCnt = 0 # # current operation count
    timing = None
    # From 9:00, n times, every t minutes, up to m people
    while currentTime <= maxMinute: # Check until business hours are over
        currentPersonCnt = 0
        currentCnt += 1 
        currentBus = []
        currentTime = 540 + (currentCnt -1) * t

        # Without exceeding the number of times of operation
        # Only if the waiting person is still available
        # is not late for the departure time
        while currentPersonCnt < m and \
            timetable and \
            timetable[0] <= currentTime:
                if not timing:
                    timing = timetable[0]
                else:
                    if timing != timetable[0]:
                        timing = timetable[0]
                currentBus.append(timetable[0]) # boarding
                timetable.pop(0) # remove from waiting list
                currentPersonCnt += 1
        
        # check Interrupt timing
        if currentCnt == n:
            # if you can get on the last bus, return the bus arrival time.
            if currentPersonCnt < m:
                answer = maxMinute
            else:
            # if not, use timing variable.
                answer = timing -1
            break
    answer = minutesToString(answer)
    return answer

# '09:00' -> 540
def stringToMinutes(time):
    minutes = 0
    minutes += int(time[:2]) * 60
    minutes += int(time[3:])
    return minutes

# 540 -> '09:00'
def minutesToString(minutes):
    hour = minutes // 60
    minute = minutes % 60
    string = str(hour).zfill(2) + ':' +str(minute).zfill(2)
    return string
    
if __name__ == "__main__":
    # From 9:00, n times, every t minutes, up to m people
    solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03'])  # 09:00
    solution(2, 10, 2, ['09:10', '09:09', '08:00']) # 09:09
    solution(2, 1, 2, ['09:00', '09:00', '09:00', '09:00']) # 08:59
    solution(1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']) # 00:00
    solution(1,1,1, ['23:59']) # 09:00
    solution(10, 60, 45, ['23:59','23:59', '23:59', '23:59', '23:59', '23:59', '23:59', \
            '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']) # 18:00