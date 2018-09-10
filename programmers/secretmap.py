"""
    (2017) KAKAO BLIND RECRUITMENT 
    [1차] 비밀지도
    https://programmers.co.kr/learn/courses/30/lessons/17681

    solution.
    1. 기본적인 비트 연산 처리법을 안다면 풀 수 있는 문제이다.
        문제에서도 비트 연산에 대한 처리임을 알려주고 있고, 
        비트 or 연산법을 사용하여, 한번이라도 1로 표시된 부분이라면 '#'로 출력되도록 처리 할 수 있다.
    ---------------------------------------------------------------------
    간단한 비트 연산.
    bin(정수 | 정수) : 두 정수의 2진수에 대한 or 연산 (둘 중 하나라도 1이면 그건 1)
    bin(정수 & 정수) : 둘다 1이면 1, 아니면 0
    bin( ^) : XOR 연산, 각 자릿수를 비교하여 다르면 1, 같으면 0

    zfill()로 앞에 0 채우기.
    bin(3)[2:].zfill(6) 
        - 2진수로 변환 : bin(3) # '0b11'
        - 변환한 2진수 잘라내기 : bin(3)[2:] # '11'
        - 잘라낸 2진수 앞에 원하는 만큼 0 추가하기 : bin(3)[2:].zfill(6) # 000011

    파이썬의 진법 변환.
    print bin(num) # 10진수 -> 2진수 변환 : 0b11000000111001
    print oct(num) # 10진수 -> 8진수 변환 : 030071
    print hex(num) # 10진수 -> 16진수 변환 : 0x3039 
    print int(bin(num),2) # 2진수 -> 10진수 변환 : 12345 
    print int(hex(num),16) # 16진수 -> 10진수 변환 : 12345
    ---------------------------------------------------------------------
"""

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:].zfill(n) # '11111'
        string = ''
        for j in range(n):
            if num[j] == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)
    return answer

if __name__ == "__main__":
    # result : ["#####","# # #", "### #", "# ##", "#####"]
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))