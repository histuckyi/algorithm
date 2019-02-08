"""
백준 11047. 동전 0
blog : https://daimhada.tistory.com/36
problem : https://www.acmicpc.net/problem/11047
"""
import sys

def greedy(bank, k):
    count = 0
    bank = list(reversed(bank))
    total = k

    for coin in bank:
        if total % coin >= 0 and total >= coin:
            cnt = total // coin
            count += cnt
            total -= cnt * coin
        if total == 0:
            break
    return count


if __name__ == "__main__":
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    bank = []
    for i in range(n):
        coin = int(sys.stdin.readline().strip())
        if coin > k:
            break
        bank.append(coin)
    print(greedy(bank, k))