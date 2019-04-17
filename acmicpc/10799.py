import sys
input = sys.stdin.readline


def solve(string):
    stack = []
    count = 0
    for i in range(0, len(string)):
        before_ch = None
        if 0 < i:
            before_ch = string[i-1]
        curr_ch = string[i]
        next_ch = None
        if i < len(string)-1:
            next_ch = string[i+1]

        if curr_ch == '(':
            # 레이저
            if next_ch == ')':
                # 스택이 채워져 있으면 막대기가 범위 내에 레이저가 있다는 의미
                if stack:
                    stack[-1] += 1
            elif next_ch == '(':
                # 막대기 시작
                stack.append(0)

        elif curr_ch == ')':
            # 막대기 끝
            if before_ch == ")":
                laser_count = stack.pop()
                count += (laser_count + 1)
                if stack:
                    stack[-1] += laser_count
    return count



if __name__ == "__main__":
    # print(solve(input().strip()))
    print(solve("()(((()())(())()))(())"))
    print(solve("(((()(()()))(())()))(()())"))