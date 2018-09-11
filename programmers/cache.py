"""
    (2017) KAKAO BLIND RECRUITMENT 
    [1차] 캐시
    https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3

    solution.
    1. 큐로 사용할 리스트를 선언한다(dictionary에는 우선순위를 표현할 index가 없으므로 큐를 사용했다)
    2. cities에 담긴 값을 하나씩 꺼내어, queue에 이미 그 값이 있는지 없는지를 확인한다.
    3. 이때 대소문자 구분 없도록 '단어'.lower() 할수를 사용하여 모두 소문자로 바꿔준다.
    4. index 값이 작을 수록 사용한지 오래된 도시명이며,
        index 값이 클 수록 최신이거나 hit가 일어난 도시명이다.
    5. 큐에 city가 있으면 (캐시 히트)
        해당 도시를 맨 뒤로 옮겨준다
    6. 큐에 city가 없으면, (캐시 미스)
        큐(캐시)가 꽉 차 있으면 맨 앞 도시를 pop해주고 맨뒤에 새로운 도시를 넣어준다.
        큐(캐시)의 크기가 0 이상일 경우에만 큐에 넣어준다.
    7. 캐시히트가 일어나면 answer에 1을 더하고,
        캐시미스가 일어나면 answer에 5를 더하여 최종적으로 그 값을 반환한다.
"""

def solution(cacheSize, cities):
    queue = [] # use an ordered container
    answer = 0
    for c in cities:
        city = c.lower()
        if city in queue:
            # cache hit
            index = queue.index(city)
            queue.pop(index)
            queue.append(city)
            answer += 1
        else:
            
            # cache miss
            if cacheSize and len(queue) >= cacheSize:
                queue.pop(0)
                queue.append(city)
            else:
                if cacheSize > 0:
                    queue.append(city)
            answer += 5
    print(answer)

if __name__ == "__main__":
    solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])  # 50
    solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']) # 21
    solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']) # 60
    solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']) # 52
    solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']) # 16
    solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']) # 25