"""
SW Expert Academy 1206. View
blog : https://daimhada.tistory.com/75
"""

def solve(arr):
    count = 0
    for i in range(2, len(arr) - 2):
        height = arr[i]
        left = max(arr[i-2:i])
        # 왼쪽 조망권 확인
        if height < left:
            continue
        right = max(arr[i+1:i+3])
        # 오른쪽 조망권 확인
        if height < right:
            continue
        around_height = max(left, right)
        count += (height - around_height)
    return count


if __name__ == "__main__":
    for i in range(10):
        c = int(input().strip())
        array = list(map(int, input().strip().split()))
        print("#{0} {1}".format(i+1, solve(array)))
