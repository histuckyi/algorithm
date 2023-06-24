"""
2358. Maximum Number of Groups Entering a Competition

문제
학생들의 성적이 정렬되지 않은 채 grades 배열로 주어진다.
학생들의 성적을 아래의 기준으로 그룹화하고 최대 몇 개의 그룹을 생성할 수 있는지 반환하는 문제이다. 
- 그룹원의 수는 순서대로 증가되어야 한다. 
- 그룹원들의 성적 합은 그룹원의 수가 적을수록 더 낮아야 한다. 
  
이해 돕기
문제를 이해하는 것도 중요하지만 그 안에서 규칙을 발견해야만 쉽게 풀 수 있다.
문제대로 로직을 구현하면 시간초과가 발생할 가능성이 크다. 

예시1을 보면, 
grades = [10,6,12,7,3,5], 결과는 3이다. 
예시의 설명처럼 (12), (6,7), (10,3,5)로 세 그룹으로 나눌수 있다.
그러나 이렇게 그룹화하는 것만이 정답은 아니다. 
(3), (5,6), (7,10,12)로도 그룹화할 수 있다. 
그 말은 즉, 그룹의 수는 동일하더라도 그룹원의 점수는 다를 수 있단 말이다. 
그리고 예시만 보면 최고점을 먼저 선택해야 하나? 라는 함정에 빠질 수 있다!
우리는 어떤 점수끼리 그룹화 했느냐 보다 '최대' 몇 개의 그룹을 생성할 수 있느냐에 초점을 맞춰서 문제를 풀어야 한다.
 
풀이
문제에 따르면 그룹원의 수는 반드시 순서대로 증가되어야 하므로,
학생 수가 6일 경우 최대한 많은 그룹으로 나눴을 때 1명, 2명, 3명으로 그룹화할 수 밖에 없다.
문제를 풀다 보면 알게 되는 게 사실상 점수는 큰 상관이 없다. 
[1,1,1,1,1,1]로 가정해서 생각해도 된다.
여기선 인원수 조건에 맞춰서 '최대' 몇 개의 그룹을 생성할 수 있느냐가 중요하다. 
그래도 이해하기 쉽게 [1,2,3,4,5,6]으로 학생의 점수를 정렬해서 생각해보자.
정렬된 학생들의 점수 덕분에 앞선 그룹원의 합이 뒷 그룹의 합보다 항상 작다는 것을 보장할 수 있다.

그룹원의 수는 1씩 증가시키면 가장 많은 그룹을 생성할 수 있다.
유일하게 주의할 건, 현재 그룹을 생성할 때 남은 학생의 수를 체크해서 다른 그룹을 생성할 만큼 학생들이 남았는지 체크해야 한다는 건데,
이때 남은 학생의 수가 너무 적을 경우에 지금 생성하는 그룹에 학생수를 포함시켜주면 된다.
그리고 지금까지 생성된 학생 수를 반환해준다.
"""
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        total_student_count = len(grades)
        if total_student_count == 0: return 0
        expected_group_member_cont = 1
        group_count = 0
        while True:
            group_count += 1
            extra_student_count = total_student_count - expected_group_member_cont
            if extra_student_count < (expected_group_member_cont + 1):
                return group_count
            total_student_count = extra_student_count
            expected_group_member_cont += 1
        return group_count
