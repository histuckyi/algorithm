"""
백준 11399. ATM
blog : https://daimhada.tistory.com/33
problem : https://www.acmicpc.net/problem/11399
"""
import sys

def greedy(line):
    total_time = 0
    waiting_time = 0
    line.sort()
    for time in line:
        waiting_time += time
        total_time += waiting_time
    return total_time


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = list(map(int, sys.stdin.readline().strip().split()))
    print(greedy(line))
