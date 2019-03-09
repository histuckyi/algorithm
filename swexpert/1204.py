"""
SW Expert Academy 1204. 최빈수 구하기
blog : https://daimhada.tistory.com/74
"""


def solve(arr):
    max_val_count = 0
    max_val = 0
    for i in range(100, -1, -1):
        count = arr.count(i)
        if max_val_count < count:
            max_val_count = count
            max_val = i
    return max_val


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        c = int(input())
        array = list(map(int,input().strip().split()))
        print("#{0} {1}".format(c, solve(array)))
