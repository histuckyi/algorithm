"""
백준 14501. 퇴사
blog : https://daimhada.tistory.com/91
problem : https://www.acmicpc.net/problem/14501
"""

# 모든 경우의 수를 구하고 그 안에서 답을 찾는다
def solve(n, tlist, plist):

    max_fee = 0
    for i in range(0, 1 << n):
        d = n  # 남은 퇴사일
        result = 0
        counsel_d = 0
        for j in range(0, n):

            if i & (1 << j):
                # counsel is over
                if counsel_d == 0:
                    # 남은 퇴사일보다 남은 상담 환자들의 상담기간이 적을 경우
                    if d >= tlist[j]:
                        # 상담 진행
                        counsel_d = tlist[j]
                        result += plist[j]

            # 상담이 예정되어 있으면 상담 진행
            if counsel_d:
                counsel_d -= 1
            d -= 1 # 하루가 흘러감

        if max_fee < result:
            max_fee = result
    return max_fee


if __name__ == "__main__":
    n = int(input().strip())
    tlist = []
    plist = []
    for i in range(n):
        t, p = input().strip().split()
        tlist.append(int(t))
        plist.append(int(p))
    print(solve(n, tlist, plist))