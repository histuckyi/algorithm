"""
백준 1946. 신입사원
blog : https://daimhada.tistory.com/39
problem : https://www.acmicpc.net/problem/1946
"""
import sys

def gen(case_num):
    for i in range(case_num):
        n = int(sys.stdin.readline().strip())
        records = []
        for j in range(n):
            report, interview = map(int, sys.stdin.readline().strip().split())
            records.append((report, interview))
        records = sorted(records, key=lambda record: record[0])
        yield records

def greedy(records):
    count = 0
    min_interview_record = 567850687058670507
    for idx, record in enumerate(records):
        if record[1] < min_interview_record:
            min_interview_record = record[1]
        if record[0] == 1 or record[1] == 1:
            count += 1
            continue

        if record[1] > min_interview_record:
            continue
        count += 1
    return count

if __name__ == "__main__":
    case_num = int(sys.stdin.readline().strip())
    for records in gen(case_num):
        print(greedy(records))
