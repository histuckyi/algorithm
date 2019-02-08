"""
백준 1758. 알바생 강호
blog : https://daimhada.tistory.com/40
problem : https://www.acmicpc.net/problem/1758
"""
import sys

def greedy(tipList):
    total_tip = 0
    for idx, tip in enumerate(tipList):
        real_tip = tip - ((idx + 1) - 1)
        if real_tip <= 0:
            break
        total_tip += real_tip
    return total_tip


if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    tipList = []
    for i in range(0, n):
        tip = sys.stdin.readline().strip()
        tipList.append(int(tip))
    tipList.sort(reverse=True)
    print(greedy(tipList))