"""
SW Expert Academy 1209. Sum(D3)
blog : https://daimhada.tistory.com/73
"""
def sumArray(array):
    max, vr, vl = 0 , 0, 0

    for i in range(0, num):
        vr += array[i][i]
        vl += array[num - i - 1][i]

        # row
        r = sum(array[i])

        # column
        c = 0
        for j in range(0, num):
            c += array[j][i]

        if max < r:
            max = r

        if max < c:
            max = c

    # Diagonal comparison
    if max < vr:
        max = vr

    if max < vl:
        max = vl

    return max


if __name__ == "__main__":
    num  = 100
    for tc in range(10):
        t = int(input())
        array = []
        for i in range(num):
            array.append(list(map(int, input().strip().split())))
        print('#{0} {1}'.format(t, sumArray(array)))
